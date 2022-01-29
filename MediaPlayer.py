from abc import ABC,abstractmethod
from dataclasses import dataclass


@dataclass
class Media:
    name : str
    location : str
    rate : float
    

   
class MediaPlayer(ABC):
    file_location_param=None
    
    def __init__(self, media_list : list  ) -> None:
        """
        creating with list of medias
        """
        
        self.play_list = []
        for elm in media_list :
            if elm.location.startswith(self.file_location_param) :
                self.play_list.append(elm)
                
    
    @property
    def playlist(self):
        
        """
            returning all playlist

        """
        
        return self.play_list
    
    @playlist.setter
    def playlist(self, media_obj :Media) :
        """
        add a single music to play list
        
        Args:
            media_obj (Media): [description]
            
        """
        if media_obj.location.startswith(self.file_location_param) :
            self.play_list.append(media_obj)
                

    
    def delete_music(self, obj_name : str) :
        """
            delete a single track in playlist
        
        Args:
            obj_name (str): [description]
        """
        for elm in self.play_list:
            if elm.name == obj_name:
                self.play_list.remove(elm)
                
                

    def play_with_name(self):
        """
        
        playing in name order 
        
        """
        
        self.play_list = sorted(self.play_list, key = lambda music : music.name )
        print ("Playing in name order ....")
        self.play()
    
    
    def play_with_rate(self):
        """
        
        playing in rate order 
        
        """
        self.play_list = sorted(self.play_list, key = lambda music : music.rate , reverse=True )
        print ("Playing in rating order ....")
        self.play()
    
    
    
    
    
    @abstractmethod
    def play(self):
        """
        abstract method for playing
        
        """
        pass
    
    
    

class WebMediaPlayer(MediaPlayer):
    file_location_param="https://"
    
    def play(self):
        
        for elm in self.play_list:
            return f"{elm.name} with rate *{elm.rate}* is playing ... location:{elm.location}"
            
            

class LocalMediaPlayer(MediaPlayer):
    file_location_param=("C:\\" , "/")
    
    def play(self):
        
        for elm in self.play_list:
            return f"{elm.name} with rate *{elm.rate}* is playing ... location:{elm.location}"
            
            
            
   
   

"in test file i did checked too"
         
media1 = Media("music","https://from-hell.com",5)
media2 = Media("amusic","/home/music",2)
media3 = Media("music","/",4.5)
media4 = Media("zmusic","C:\musics",2.5)
media5 = Media("amusic","https://form-no-where",4.5)

play_list1 = [media1,media2,media3,media4,media5]


webmediaplayer = WebMediaPlayer(play_list1)



print(webmediaplayer.play())

print(webmediaplayer.play_with_name())
print(webmediaplayer.play_with_rate())

print("----------------------------------------")

localmediaplayer = LocalMediaPlayer(play_list1)

localmediaplayer.playlist=Media("newmusic","/music",5)

print(localmediaplayer.play())
print(localmediaplayer.play_with_name())
print(localmediaplayer.play_with_rate())