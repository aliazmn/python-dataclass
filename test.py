import unittest

from MediaPlayer import Media,WebMediaPlayer,LocalMediaPlayer



class SimpleTest(unittest.TestCase):
    
    def setUp(self) -> None:
        media1 = Media("music","https://from-hell.com",5)
        media2 = Media("amusic","/home/music",2)

        self.play_list1 = [media1,media2]
        
    def test_webmusic(self):
        self.webmediaplayer = WebMediaPlayer(self.play_list1)
        self.assertEqual(self.webmediaplayer.play(),"music with rate *5* is playing ... location:https://from-hell.com")
    
    def test_localmusic(self):
        self.localmediaplayer = LocalMediaPlayer(self.play_list1)

        self.assertEqual(self.localmediaplayer.play(),"amusic with rate *2* is playing ... location:/home/music")
        
        
        

if __name__ == "__main__":
    unittest.main()