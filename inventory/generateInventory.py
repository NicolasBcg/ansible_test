
ouis=["o","oui","y","yes","uoi","ou","ui","eys","yse"]#liste d'entrees utilisateurs etants considerees comme etant "oui"
def main():
    vars=["ansible_connection","ansible_network_os","ansible_user","ansible_password"]
    varsUsed=[]
    print("----[creation d'un inventaire en .yml avec pour host mikrotiks]----")
    inventory="mikrotiks:\n"
    inventory+="  hosts :\n"
    no_vars=True

    while(input("\nVoulez-vous ajouter un hote ? [default non] : ").lower().strip() in ouis):
        host=input("adresse IP de l'hôte : ").strip()
        inventory+="    "+host+" :\n"
        varDispos=vars
        while(input("\nVoulez-vous ajouter une variable pour l'hote "+host+" ? [default non] : ").lower().strip() in ouis):
            print("\nles variables disponibles sont : ")
            for i in range(len(varDispos)):
                print("entrez "+str(i)+" pour : "+varDispos[i])
            selectedvar=varDispos.pop(int(input("\nQuelle variable voulez vous : ").strip()))
            inventory=inventory+str(varsAsignation(selectedvar))
            varsUsed.append(selectedvar)
            
    varDispos= list(set(vars)-set(varsUsed))
    print("\nvariables encore attribuables : "+str(varDispos))
    while(input("Voulez-vous ajouter une variable globale ? [default non] : ").lower().strip() in ouis):
        if no_vars:
            inventory+="  vars:\n"
            no_vars=False
        print("\nles variables disponibles sont : ")
        for i in range(len(varDispos)):
            print("entrez "+str(i)+" pour : "+varDispos[i])
        selectedvar=varDispos.pop(int(input("Quelle variable voulez vous : ").strip()))
        inventory=inventory+str(varsAsignation(selectedvar))
        print("\nvariables encore attribuables : "+str(varDispos))
            

    
    yaml_file = open("/home/ansible/inventory/"+input("nom sous lequel enregistrer l'inventaire : ")+".yml", 'w')
    yaml_file.write(inventory)
    yaml_file.close()

def varsAsignation(selectedvar):
    if selectedvar == "ansible_connection":
        print("ansible_connection = ansible.netcommon.network_cli")
        return "      ansible.netcommon.network_cli\n"
    elif selectedvar == "ansible_network_os": 
        print("ansible_network_os = community.routeros.routeros")
        return "      community.routeros.routeros\n"
    else :
        return "      "+selectedvar+": "+input("Quelle valeur voulez vous pour "+selectedvar+" : ").strip()+"\n"

if __name__ == "__main__":
    main()

