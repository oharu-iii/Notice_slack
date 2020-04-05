import subprocess
import sys
# from pathlib import Path

if __name__ == "__main__":
    args = sys.argv
    # base = Path(__file__).parent
    # py_file = base.joinpath(args[1])

    try:
        # subprocess.check_call(['python', str(py_file.resolve())])
        subprocess.check_call(['python', args[1]])
        print('End.')
    except subprocess.CalledProcessError:
        print('bad.')
