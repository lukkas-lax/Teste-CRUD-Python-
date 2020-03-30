'''
Created on 29 de mar de 2020

@author: lukit
'''
from Testes import DAO_Equipamento
if __name__ == '__main__':
    ans=True
    while ans:
        print("""
        1.Inserir Equipamento
        2.Selecionar Todos
        3.Selecionar por ID
        4.Alterar Equipamento
        5.Excluir Equipamento
        6.Exit/Quit
        """)
        ans=input("Selecione a sua opcao: ")
        
        if ans=="1":
            DAO_Equipamento.inserir()
            print("\nEquipamento inserido")
            
        elif ans=="2":
            DAO_Equipamento.selecionar()
            print("\n Todos Selecionados")
            
        elif ans=="3":
            DAO_Equipamento.selecionarChave()
            print("\n Equipamento selecionado")
            
        elif ans=="4":
            DAO_Equipamento.update()
            print("\n Equipamento alterado")
            
        elif ans=="5":
            DAO_Equipamento.excluir()
            print("\n Equipamento excluido")
            
        elif ans=="6":
            print("\n Saindo") 
            ans = None
        else:
            print("\n Opcao invalida")