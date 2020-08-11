class Personnage:
	
	def __init__(self, nom):
		self.nom=nom
		
		
	def __str__(self):
		return "Nom :{0}".format(self.nom)
		

	
		
class AgentSecret(Personnage):
	
	
	def __str__(self):
		return "AGENT : Nom :{0}".format(self.nom)
		

	"ON EST LAAAAAAA"







































