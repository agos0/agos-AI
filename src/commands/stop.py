def stop_command(message, client):
    return '!stop' in message.content and message.author != client.user