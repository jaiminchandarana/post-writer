import sys
import warnings
from post_writer.crew import PostWriter
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def choice():
    topic = input("Enter a plateform to write post for : ")
    description = input("Provide some information of your project : ")
    code = input("paste your main file here(optional) : ")
    if not topic or not description:
        print("Enter plateform and information of your project.\n")
        return choice()
    return topic,description,code

topic,description,code = choice()

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': f'{topic}',
        'description' : f'{description}',
        'code' : f'{code}'
    }
    
    try:
        PostWriter().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'topic': f'{topic}',
        'description' : f'{description}',
        'code' : f'{code}'
    }
    try:
        PostWriter().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        PostWriter().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'topic': f'{topic}',
        'description' : f'{description}',
        'code' : f'{code}'
    }
    
    try:
        PostWriter().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
