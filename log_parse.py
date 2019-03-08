import os
import shutil
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configparser import ConfigParser

Base = declarative_base()

# http://g.recordit.co/tjl5YvR0xI.gif
class Message(Base):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True)
    time = Column(DateTime, nullable=False, default=datetime.utcnow())
    user = Column(String(50), nullable=False)
    channel = Column(String(50), nullable=False)
    content = Column(String(500), nullable=False)


def main():

    config = ConfigParser()

    # Try to find the config file, if it does not exist, create one.
    if not os.path.exists(os.path.join(os.getcwd(), 'config.ini')):

        create_config(config)

    else:

        config.read('config.ini')

    # Configuration
    db_name = config['PARSER-SETTINGS']['database_name'] + '.db'
    log_folder = config['PARSER-SETTINGS']['new_logs']
    processed_log_folder = config['PARSER-SETTINGS']['old_logs']

    log_dir, parsed_dir = folder_setup(log_folder, processed_log_folder)

    engine = create_engine('sqlite:///' + db_name)

    # Make the DB if it is not in our CWD.
    if not os.path.exists(os.path.join(os.getcwd(), db_name)):
        Base.metadata.create_all(engine)

    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    errors = 0
    successes = 0

    total_start_time = datetime.now()

    list_files = os.listdir(log_dir)

    if len(list_files) < 1:

        print('No files to process.')
        print('Exiting.')
        exit(0)

    else:

        for file in list_files:

            file_start_time = datetime.now()

            log_file = open(os.path.join(log_dir, file), 'r', encoding='utf-8')

            # Process each line
            for line in log_file:

                try:
                    # Extract the data we want
                    time, channel, username, message = parse_line(line)

                    message_db = Message(time=time,
                                         content=message[:500],
                                         user=username,
                                         channel=channel)

                    session.add(message_db)

                except ValueError as e:

                    errors = errors + 1
                    print(f'ValueError: {e}')
                    continue

                except IndexError:
                    # todo len()?
                    errors = errors + 1
                    continue

                successes = successes + 1

            # Close the file, we're finished and need to move it.
            log_file.close()

            # Move to 'old_logs/'.
            shutil.move(os.path.join(log_dir, file), os.path.join(parsed_dir, file))

            # Time when we have parsed an individual file and saved it to the db.
            file_end_time = datetime.now()

            print(f'File {file} done. Processed in: {file_end_time - file_start_time}')

            # Save all additions we made using that file.
            session.commit()

    total_end_time = datetime.now()

    print(f'\n------- RUN INFORMATION -------\n'
          f'Execution Time: {total_end_time - total_start_time}\n'
          f'Success: {successes}\n'
          f'Errors: {errors}\n'
          f'Error percentage: {100 * float(errors)/float(errors+successes):.2f}%\n')

    print('Done.')


def parse_line(line):
    """
    Extract all the data we want from each line.

    :param line: A line from our log files.
    :return: The data we have extracted.
    """

    time = line.split()[0].strip()
    response = line.split(' :')
    message = response[len(response) - 1].strip('\n')
    channel = response[1].split('#')
    username = channel[0].split('!')
    username = username[0]
    channel = channel[1]
    time = datetime.strptime(time, '%Y-%m-%d_%H:%M:%S')

    return time, channel, username, message


def folder_setup(log_folder, processed_log_folder):
    """
    Creates the folder structure if it does not exist already and then
    returns the paths to these folders.

    :param log_folder: The folder that new log files will be put in.
    :param processed_log_folder: The folder that processed log files will be put in.
    :return: The paths to these folders.
    """

    if log_folder is processed_log_folder:
        print(f"Log folder '{log_folder}' and '{processed_log_folder} are\n"
              f"the same. Please choose different folders.")
        print('Exiting.')
        exit(0)

    # Where new logs are stored.
    log_dir = os.path.join(os.getcwd(), log_folder)

    # Where to put logs after they have been processed.
    parsed_dir = os.path.join(os.getcwd(), processed_log_folder)

    if not os.path.exists(log_dir):
        os.mkdir(log_dir)

    if not os.path.exists(parsed_dir):
        os.mkdir(parsed_dir)

    return log_dir, parsed_dir


def create_config(config):
    """
    Creates a fresh config file with the needed parameters.

    :param config: a ConfigParser() object.
    """

    config['PARSER-SETTINGS'] = {'database_name': 'twitch_logs',
                                 'new_logs': 'logs_new',
                                 'old_logs': 'logs_old'}

    with open('config.ini', 'w') as new_config_files:

        config.write(new_config_files)


if __name__ == '__main__':
    main()
