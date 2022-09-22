Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def is_valid(self, var, color):
...     territory = self.map[var]
... 
...     for neighbor in territory.neighbors:
...         if color == self.map[neighbor].color:
...             return False
... 
...     return True
... 
... def set_map(self, key, color):
...     self.map[key].color = color
... 
... def remove_from_domains(self, key, color):
...     territory = self.map[key]
... 
...     for var in territory.neighbors:
...         if self.map[var].color != None:
...             continue
...         if color in self.domains[var]:
