session = {}

def add_message(sessionID, role, content):
    if sessionID not in session:
        session[sessionID] = []
    session[sessionID].append(
        {"role" : role ,
         "content" : content}
    )

def get_history(sessionID):
    return session[sessionID]

def format_history(sessionID):
    formatted_history = ""
    for message in session[sessionID]:
        formatted_history += f'{message["role"]} : {message["content"]}\n'
    return formatted_history
