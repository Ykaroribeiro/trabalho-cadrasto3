import os

LISTA = []

## Carrega a lista do arquivo
# Abre o arquivo (se ele já existe)
if os.path.exists("crud.txt"):
    # Abre o arquivo para leitura ('r' -> read)
    file = open("crud.txt", 'r')
    # Lê o arquivo linha por linha e coloca na lista
    for item in file.readlines():
        LISTA.append(item[:-1]) # Esse [:-1] tira o último caractere, um "\n"
    # Fecha o arquivo
    file.close()
## Salva a lista no arquivo
# Abre o arquivo para escrita ('w' -> write)
file = open("crud.txt", 'w')
# Itera a lista e escreve cada item no arquivo
for item in LISTA:
    # O str() converte o item em uma string
    # O '\n' no final é uma quebra de linha, pra cada item sair numa linha
    file.write(str(item) + '\n')
# Fecha o arquivo
file.close()
x=0
while x==0:
    op1=input("Pressione Enter para começar: ")
    if op1=="":
    	a=0
    	modelo=[]
    	marca=[]
    	ano=[]
    	placa=[]
    	valor=[]
    	print("-----------------------------------------------------------------------\n")
    	print("                         Programa CRUD.txt")
    	qtc=0
    	while a==0:
    		print("\n","="*27," MENU INICIAL ","="*27)
    		print("1-Cadastrar")
    		print("2-Ler")
    		print("3-Deletar")
    		print("4-Atualizar")
    		print("5-Sair")
    		esc=input("Escolha a opção que deseja:\n")
    		if esc=="1":
    			c=0
    			if qtc==0:
        			while c==0:
        				print("__"*35)
        				qtc=int(input('Quantos cadastros você quer fazer?\n '))
        				if qtc>0:
        				    print("__" *35)
        				    print("Preencha os espaços abaixo para fazer o seu cadastro:")
        				    print("__"*35)
        				    qt=1
        				    registro=0
        				    while  registro<qtc:
        				        print("__"*5,"Cadastro %s"%qt,"__"*5)
        				        mo=input("Digite seu modelo: ")
        				        ma=input("Digite sua marca: ")
        				        an=input("Digite seu ano: ")
        				        pl=input("Digite sua placa: ")
        				        va=input("Digite seu valor: ")
        				        print("__" *35)
        				        print("Deseja continuar o cadastro com essas informações ou deseja refazer? ")
        				        l=0
        				        while l==0:
        				            print("1-Salvar")
        				            print("2-Refazer")
        				            i=int(input("Digite sua escolha: "))
        				            print("__"*35)
        				            if i==1:
        				                if mo=="" or ma=="" or an=="" or pl=="" or va=="":
        				                    print("!!Há campos vazios!!")
        				                    print("Por favor preencha os campos corretamente")
        				                    print("__" *35)
        				                    l=1
        				                else:
        				                    print("  "*13 ,"Dados salvos")
        				                    modelo.append(mo)
        				                    marca.append(ma)
        				                    ano.append(an)
        				                    placa.append(pl)
        				                    valor.append(va)
        				                    if qt==qtc:
        				                        l=1
        				                        c=1
        				                        registro+=1
        				                    else:
        				                        l=1
        				                        qt+=1
        				                        registro+=1
        				            elif i==2:
        				                    print("Refazer cadastro")
        				                    l=1
        				                    registro=registro
        				            else:
        				                print("  "*13 ,"Sem função")
        				else:
        					print("Número de cadastros invalido")
        					c=0
    			elif qtc!=0:
    			    print("__" *35)
    			    print("Você já tem cadastros feitos!!")
    			    print("__" *35)
    			    k=0
    			    while k==0:
    			        print("Você deseja: ")
    			        print("1-Adicionar cadastros")
    			        print("2-Valtar ao menu inicial")
    			        i=int(input("Escolha sua opção: "))
    			        print("__" *35)
    			        if i==1:
    			            while c==0:
                				print("__"*35)
                				qtc2=int(input('Digite:\n "0" se quiser voltar ao menu\n ou\n Quantos cadastros você quer fazer:\n '))
                				if qtc2>0:
                						print("__" *35)
                						print("Preencha os espaços abaixo para fazer o seu cadastro:")
                						print("__"*35)
                						qtc3=qtc2+qtc
                						qt2=qtc+1
                						registro=0
                						while  registro<qtc2:
                							print("__"*5,"Cadastro %s"%qt2,"__"*5)
                							mo=input("Digite seu modelo: ")
                							ma=input("Digite sua marca: ")
                							an=input("Digite seu ano: ")
                							pl=input("Digite sua placa: ")
                							va=input("Digite seu valor: ")
                							print("__" *35)
                							print("Deseja continuar o cadastro com essas informações ou deseja refazer? ")
                							l=0
                							while l==0:
                							    print("1-Salvar")
                							    print("2-Refazer")
                							    d=input("Digite sua escolha: ")
                							    print("__"*35)
                							    if d=="1":
                							        if i==1:
                							            if mo=="" or ma=="" or an=="" or pl=="" or va=="":
                							                print("!!Há campos vazios!!")
                							                print("Por favor preencha os campos corretamente")
                							                print("__" *35)
                							                l=1
                							            else:
                							            	print("  "*13 ,"Dados salvos")
                							            	modelo.append(mo)
                							            	marca.append(ma)
                							            	ano.append(an)
                							            	placa.append(pl)
                							            	valor.append(va)
                							            	qtc+=1
                							            	qt2+=1
                							            	if qt2==qtc3+1:
                							            	    registro+=1
                							            	    l=1
                							            	    c=1
                							            	    k=1
                							            	else:
                							            	    registro+=1
                							            	    l=1
                							    elif d=="2":
                							        print("Refazer cadastro")
                							        registro=registro
                							        l=1
                							    else:
                							        print("  "*13 ,"Sem função")
                				elif qtc2==0:
                				    c=1
                				    k=1
                				else:
                				    print("Número de cadastros invalido")
                				    c=0
    			        elif i==2:
    			            k=1
    			        else:
    			            print("  "*13 ,"Sem função")
    		elif esc=="2":
    			if qtc!=0:
    				registro=0
    				qr=1
    				print("=="*12,"Cadastros Registrados","=="*12)
    				while registro<qtc:
    					print("__"*5,"Cadastro %s"%qr,"__"*5)
    					print("modelo: ",modelo[registro])
    					print("marca: ",marca[registro])
    					print("ano: ",ano[registro])
    					print("placa: ",placa[registro])
    					print("valor: ",valor[registro])
    					print("--"*35)
    					registro+=1
    					qr+=1
    				e=0
    				while e==0:
    					enter=input("Pressione 'Enter' para voltar ao menu:\n")
    					if enter=="":
    						e=1
    					else:
    						print("__"*35)
    						print("!!Erro na tecla digitada tente novamente!!")
    						print("--"*35)
    			elif qtc==0:
    				print("__"*35)
    				print("  "*13 ,"Sem cadastro")
    				print("__"*35)
    		elif esc=="3":
    			print("__" *35)
    			if qtc!=0:
    				u=0
    				while u==0:
    					registro=0
    					print("=="*12,"Cadastros Registrados","=="*12)
    					while registro<qtc:
    						print("-="*5,"Cadastro ",registro+1,"-="*5)
    						print("modelo: ",modelo[registro])
    						print("marca: ",marca[registro])
    						print("ano: ",ano[registro])
    						print("placa: ",placa[registro])
    						print("valor: ",valor[registro])
    						print("--"*35)
    						registro+=1
    					qcd=int(input('Digite:\n"-1" para deletar todos\nou\n"0" para voltar ao menu inicial\nou\nQual cadastro você quer deletar\n'))
    					if qcd<=qtc and qcd>0:
    					    print("Cadastro deletado")
    					    qcd-=1
    					    del modelo[qcd]
    					    del marca[qcd]
    					    del ano[qcd]
    					    del placa[qcd]
    					    del valor[qcd]
    					    qtc=qtc-1
    					    if qtc==0:
    					        u=1
    					elif qcd==0:
    						u=1
    					elif qcd==-1:
    					    print("-"*35)
    					    print("                           Todos os cadastros foram deletados")
    					    print("-"*35)
    					    modelo=[]
    					    marca=[]
    					    ano=[]
    					    placa=[]
    					    valor=[]
    					    qtc=0
    					    u=1
    					else:
    						print("__"*35)
    						print("Não há esse cadastro/Função")
    						print("__"*35)
    			else:
    				print("__"*35)
    				print("  "*13 ,"Sem cadastro")
    				print("__"*35)
    		elif esc=="4":
    			print("__" *35)
    			if qtc!=0:
    				u=0
    				while u==0:
    					registro=0
    					print("=="*12,"Cadastros Registrados","=="*12)
    					while registro<qtc:
    						print("__"*5,"Cadastro ",registro+1,"__"*5)
    						print("modelo: ",modelo[registro])
    						print("marca: ",marca[registro])
    						print("ano: ",anp[registro])
    						print("placa: ",placa[registro])
    						print("valor: ",valor[registro])
    						print("--"*35)
    						registro+=1
    					qcd=int(input('Digite "-1" para atualizar todos\nou\nDigite "0" para voltar ao menu inicial\nou\nDigite qual cadastro você quer atualizar\n'))
    					if qcd<=qtc and qcd>0:
    						t=0
    						while t==0:
    						    h=0
    						    print("-"*5,"Você está atualizado o cadastro ",qcd,"-"*5)
    						    inp=input("Digite seu novo modelo: ")
    						    inp2=input("Digite sua nova marca: ")
    						    inp3=input("Digite seu novo ano: ")
    						    inp4=input("Digite sua nova placa: ")
    						    inp5=input("Digite seu novo valor: ")
    						    while h==0:
    						        vcd=int(input("Você deseja:\n1-Salvar\n2-Refazer\n3-Voltar sem salvar\n"))
    						        if vcd==1:
    						            if inp=="" or inp2=="" or inp3=="" or inp4=="" or inp5=="":
    						                print("Há campos vazios!")
    						                print("Por favor preencha os campos")
    						                print("--"*35)
    						            else:
    						                qcd-=1
    						                modelo[qcd]=inp
    						                marca[qcd]=inp2
    						                ano[qcd]=inp3
    						                placa[qcd]=inp4
    						                valor[qcd]=inp5
    						                print("!!Todas as informações foram atualizadas!!")
    						                print("__"*35)
    						                h=1
    						                t=1
    						                u=0
    						        elif vcd==2:
    						            h=1
    						            t=1
    						            u=0
    						        elif vcd==3:
    						            h=1
    						            t=1
    						        else:
    						            print("  "*13 ,"Sem função")
    					elif qcd==0:
    					    u=1
    					elif qcd==-1 and qtc!=0:
    					    qt3=0
    					    while qt3<qtc:
    					        print("-"*5,"Você está atualizado o cadastro ",qt3+1,"-"*5)
    					        inp=input("Digite seu novo modelo: ")
    					        inp2=input("Digite sua nova marca: ")
    					        inp3=input("Digite seu novo ano: ")
    					        inp4=input("Digite sua nova placa: ")
    					        inp5=input("Digite seu novo valor: ")
    					        h=0
    					        while h==0:
    					            vcd=int(input("Você deseja:\n1-Salvar\n2-Refazer\n"))
    					            if vcd==1:
    					                if inp=="" or inp2=="" or inp3=="" or inp4=="" or inp5=="":
    						                print("!!Há campos vazios!!")
    						                print("Por favor preencha os campos")
    						                h=1
    						                print("--"*35)
    					                else:
    						                modelo[qt3]=inp
    						                marca[qt3]=inp2
    						                ano[qt3]=inp3
    						                placa[qt3]=inp4
    						                valor[qt3]=inp5
    						                print("As informações foram atualizadas")
    						                print("__"*35)
    						                h=1
    						                qt3+=1
    					            elif vcd==2:
    					                h=1
    					            else:
    						            print("  "*13 ,"Sem função")
    					else:
    						print("_"*35)
    						print("Não á esse cadastro")
    						print("_"*35)
    			else:
    				print("__"*35)
    				print( "  "*13 ,"Sem cadastro")
    				print("__"*35)
    		elif esc=="5":
    		    ss=0
    		    while ss==0:
    			    ops=int(input("Deseja sair do programa?\n 1-Sim\n 2-Não\n "))
    			    if ops==1:
    				    print("Fechando sistema...")
    				    print("Fim do programa")
    				    a=1
    				    x=1
    				    ss=1
    			    elif ops==2:
    			        a=0
    			        ss=1
    			    else:
    			        print("Opção Inválida")
    			        ss=0
    		else:
    			print("Essa opção não existe\n==Por favor digite uma opção do menu==\n")
    else:
    	print("===Enter não pressionado===\nVocê digitou '%s'! "%op1)
    	break
    ler_cadastro.close()        
    arquivo_cadastro = open("dados.txt", 'w+', encoding="utf-8")
    arquivo_cadastro.write("%s" %dados)
    arquivo_cadastro.close()