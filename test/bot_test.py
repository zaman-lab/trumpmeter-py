
from tweepy.auth import OAuthHandler
from tweepy.streaming import Stream
#from keras.engine.training import Model

from app.bot import StdOutListener, Stream
from app.model import unweighted_model

def test_listener():
    listener = StdOutListener(model=unweighted_model()) # using unweighted model for faster tests
    assert isinstance(listener.auth, OAuthHandler)

def test_stream():
    listener = StdOutListener(model=unweighted_model()) # using unweighted model for faster tests
    stream = Stream(listener.auth, listener)
    assert isinstance(stream, Stream)
