from extraccion_dof import extraccion

def cambiar_url(self):
    url=extraccion()
    self.nva_url=input()
    url.acceso_web(self.nva_url)
    
if __name__ == "__cambiar_url__":
    cambiar_url()