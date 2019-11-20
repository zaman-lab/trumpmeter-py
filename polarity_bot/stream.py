


from tweepy import Stream

from polarity_bot.listener import StdOutListener

def stdout_stream(model):
    listener = StdOutListener(model)
    print("LISTENER", type(listener))

    stream = Stream(listener.auth, listener)
    print("STREAM", type(stream))

    return stream
