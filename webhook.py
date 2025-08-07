from flask import Flask, request
import os
import git

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    repo = git.Repo('/home/Ahmad-er-ops/simple-ci')
    origin = repo.remotes.origin
    origin.pull()
    os.system("pkill -f app.py")
    os.system("nohup python3 /home/your-username/auto-deploy-demo/app.py &")
    return 'Updated Python App\n'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

