#Créer son propre contexte

class TestContext:
    def __enter__(self):
        print('Je teste le contexte')
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print('Je sors du contexte')
        return True
    
# Utilisation de contexte
with TestContext() as context:
    print('je rentre dans le contexte')