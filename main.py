from Data.data_fetcher import data_fetcher
from agents.langflow_agent import langflow_agent

def main():
    username = 'manitejagaddam'
    project_name = 'Pupil-Dialation'
    data_fetcher(username, project_name)
    langflow_agent()
    


if __name__ == "__main__":
    main()
