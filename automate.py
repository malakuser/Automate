from graphviz import Digraph
    

dot = Digraph(comment='Ton AUTOMATE')#on crée notre diagraph à remplir 
nbr_etats = int(input("Entrez le nombre d'états de votre automate : "))
   
#on cree une fonction qui trace un automate selon l'input de l'utilisateur 
def trace_nodes():

    element_etat = [] # on crée la liste des états entrés par l'utilisateur 
    
    i = 0
    while i < nbr_etats:
            elt_etat = input(f"Entrez l'élement {i} de votre element_etat : ")
            element_etat.insert(i,elt_etat)
            a = str(i)   #la conversion de l'indice i de type int en string
            
            print("Cet état est-il final/initial ou non : ")
            
            final = "l"
            
            while final != "n" and final != "y":
                final = input("(y/n): ").lower()
            if final == "y":
                dot.node(a, elt_etat ,shape = "doublecircle")

            else :
                dot.node(a, elt_etat ,shape = "circle")
 
	   

            i=i+1
    
   
    print(f"la liste d'aphabet de votre automate est : {element_etat}")

    print(dot.source)
    


# fonction qui relie les noeuds

def relie_nodes():
    
    
    print("Maintenant entrez les noeuds à relier : \nAttention la valeur entrée doit appartenir à l'element_etat que vous avez saisi!!!!")
    nbr_liaison = int(input("Entrez le nombre de liaisons que vous voulez ajouter : "))
    i = 0 
    while i < nbr_liaison : 

        node_1 = input("Entrez le premier noeud à relier : ")
        node_2 = input("Entrez le deuxiéme noeud à relier : ")
        

        #Exemple de liaison de nodes :
        #dot.node('A', '1')
        #dot.node('B', '2')
        #dot.edges(['AB', 'AL'])
        #dot.edges(['AB', 'AL'])

        #dot.edge('B', 'L', constraint='false')
        libellé = input("Entrez la transation: ")  
        
        dot.edge(node_1 , node_2 , constraint = 'false' , label = libellé )
        
        print(dot.source)  
         #on affiche les coordonées du graphe après chaque itération 
        i=i+1
 

trace_nodes()
relie_nodes()

def ajouteNoeud():
    response = input("Voulez-vous ajouter un autre noeud : (y/n) :")

    match response :
        case "y":
            element_etat = [] # on crée la liste des états entrés par l'utilisateur 
            nbr_etats_0 = int(input("Entrez le nombre d'états que vous voulez ajouter : "))
            i = 0
            while i < nbr_etats_0 :
                elt_etat = input(f"Entrez l'élement {i+nbr_etats} de votre element_etat : ")
                element_etat.insert(i+nbr_etats,elt_etat)
                a = str(i+nbr_etats)   #la conversion de l'indice i de type int en string
                
                print("Cet état est-il final/initial ou non : ")
                
                final = "l"
                
                while final != "n" and final != "y":
                    final = input("(y/n): ").lower()
                if final == "y":
                    dot.node(a, elt_etat ,shape = "doublecircle")

                else :
                    dot.node(a, elt_etat ,shape = "circle")
    
        
                print(dot.source)
                i=i+1
           
            relie_nodes()
        
        
        case "n":
            print("Merci d'avoir utilisé ce code!!")
        case _ :
            print("Merci d'avoir utilisé ce code!!")
    
ajouteNoeud()
        