#equivalent to Cast() class in RFK

class ObjectList:
    """A collection of Game Objects.

    The responsibility of a ObjectList is to keep track of a collection of Game Objects. It has methods for 
    adding, removing and getting them by a group name.

    Attributes:
        _self._game_object (dict): A dictionary of game objects { key: group_name, value: a list of game objects }
    """

    def __init__(self):
        """Constructs a new Game Objects."""
        self._game_objects = {}
        
    def add_object(self, group, value):
        """Adds a Game Object to the given group.
        
        Args:
            group (string): The name of the group.
            actor (value): The game object.
        """

        #add an item to a list
        if not group in  self._game_objects():
             self._game_objects[group] = []
            
        #append an item inside the array for the grop created
        if not value in  self._game_objects[group]:
             self._game_objects[group].append(value)

    def get_game_objects(self, group):
        """Gets the actors in the given group.
        
        Args:
            group (string): The name of the group.

        Returns:
            List: The actors in the group.
        """
        results = []
        if group in  self._game_objects():
            results =  self._game_objects[group].copy()
        return results
    
    def get_all_game_objects(self):
        """Gets all of the actors in the cast.
        
        Returns:
            List: All of the actors in the cast.
        """
        results = []
        for group in  self._game_objects:
            results.extend( self._game_objects[group])
        return results

    def get_first_game_object(self, group):
        """Gets the first actor in the given group.
        
        Args:
            group (string): The name of the group.
            
        Returns:
            List: The first actor in the group.
        """
        result = None
        if group in  self._game_objects():
            result =  self._game_objects[group][0]
        return result

    def remove_game_object(self, group, actor):
        """Removes an actor from the given group.
        
        Args:
            group (string): The name of the group.
            actor (Actor): The actor to remove.
        """
        if group in  self._game_objects:
             self._game_objects[group].remove(actor)