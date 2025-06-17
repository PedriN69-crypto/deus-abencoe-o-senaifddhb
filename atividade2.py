import os

os.system("cls || clear")

pedido = ""
total = 0

print("""
    ================= MENU =================
    1 | Picanha    | R$40,00
    2 | Feijoada   | R$38,00
    3 | Strogonoff | R$25,00
    4 | File       | R$30,00
    5 | Lasanha    | R$15,00
    6 | churrasco  | R$20,00
    7 | Pizza      | R$8,00
    0 | Finalizar pedido
    """)

while True:
    escolha = int(input("Digite o código do prato ou 0 para finalizar: "))
    match escolha:
            case 1:
                prato = "Picanha"
                valor = 40
            case 2:
                prato = "Feijoada"
                valor = 38
            case 3:
                prato = "Strogonoff"
                valor = 25
            case 4:
                prato = "file"
                valor = 30
            case 5:
                prato = "Lasanha"
                valor = 15
            case 6:
                prato = "churrasco"
                valor = 20
            case 7:
                prato = "Pizza"
                valor = 8
            case 0:
                break
            case _:
                print("Inválido! Escolha um código de 1 a 7.")
                continue
   
    pedido += f"{prato} - R${valor:.2f}\n"
    total += valor  
    print("\nNota fiscal:")
    print(pedido)
    print(f"Subtotal (sem desconto ou acréscimo): R${total:.2f}")

while True:
    forma_pagamento = input("\nForma de Pagamento: (à vista / cartão): ").lower()
    match forma_pagamento:
        case "à vista":
            desconto = total * 0.1
            total_com_desconto = total - desconto
            print(f"Valor do desconto: R${desconto:.2f}")
            print(f"Total com desconto: R${total_com_desconto:.2f}")
            break
        case "cartão":
            acrescimo = total * 0.1
            total_com_acrescimo = total + acrescimo
            print(f"Valor do acréscimo: R${acrescimo:.2f}")
            print(f"Total com acréscimo: R${total_com_acrescimo:.2f}")
            break
        case _:
            print("Forma de pagamento inválida!")

print()
print("\nNota fiscal:")
print(pedido)
if forma_pagamento == "a vista":
    print(f"Forma de pagamento: À vista")
    print(f"Total a pagar: R${total_com_desconto:.2f}")
elif forma_pagamento == "cartao":
    print(f"Forma de pagamento: Cartão")
    print(f"Total a pagar: R${total_com_acrescimo:.2f}")