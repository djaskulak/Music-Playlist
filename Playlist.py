from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None


  # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

  def add_song(self, title):
    song_added = Song(title)
    song_added.next = self.__first_song
    self.__first_song = song_added



  # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index.
  # The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index. Otherwise, return -1.

  def find_song(self, title):
    song_playing = self.__first_song
    i = 0

    while song_playing != None:
      if song_playing.get_title() == title:
        i += 1
        return i
      elif song_playing.get_title() != title:
        i += 1
        song_playing = song_playing.next
      else: 
        pass

    return


  # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 

  def remove_song(self, title):
    current = self.__first_song
    previous = None

    while current != None:
      if current.get_title() != title:
        previous = current
        current = current.next 
      elif current.get_title() == title:
        if previous == None:
          self.__first_song = None
          print("Song Removed")
          return
        elif current.next == None:
          previous.set_next_song(None)
          print("Song Removed")
          return
        else: 
          pass
      else: 
        pass

    return



  # TODO: Create a method called length, which returns the number of songs in the playlist.

  def length(self):
    counter = 0
    current_node = self.__first_song

    while current_node != None:
      counter += 1
      current_node = current_node.get_next_song

    return counter


  # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  def print_songs(self):
    current = self.__first_song

    while current != None:
      print(current)
      current = current.next