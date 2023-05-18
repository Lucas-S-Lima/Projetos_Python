# Madlib é um jogo em que, em uma historia já existente, são deixadas lacunas para serem preenchidas pelo usuário, de modo a criar uma história divertida e única. Vamos ver para onde suas respostas vão te levar!

print("Responda 16 perguntas e veja sua história ganhar vida!")
print()

ano = input("1. Digite um ano: ")
fazenda = input("2. Dê um nome a uma fazenda: ")
cidade = input("3. Nome de uma cidade: ")
nome_mulher = input("4. Nome feminino: ")
nome_prato = input("5. Nome de um prato de comida: ")
animal = input("6. Nome de um animal: ")
comida_animal = input("7. Algo que se pode comer: ")
lugar_marido = input("8. Lugar em uma fazenda: ")
nome_homem = input("9. Nome masculino: ")
lugar_pegou_coisa = input("10. Lugar para se guardar coisas: ")
arma_ferramenta = input("11. Utensilio, arma ou ferramenta: ")
lugar_busca = input("12. Lugar para se procurar algo perdido: ")
lugar_animal_estava = input("13. Lugar onde se esconder: ")
numero = input("14. Digite um número: ")
lugar_voltou = input("15. Se você estivesse cansado, para onde iria?: ")
estado = input("16. Digite uma emoção (ex: feliz ou assustado(a): ")

print()
print(40 * ">>>")
print()

madlib = f"No ano de {ano}, existia uma fazenda chamada {fazenda}, no interior de uma cidadezinha chamada {cidade}. Certo dia, quando a Sra. {nome_mulher} acordou pela manhã e foi tirar os ovos do galinheiro para fazer um {nome_prato}, ela encontrou um(a) enorme {animal}, que havia comido todas as suas {comida_animal}. Ao se deparar com aquele gigantesco(a) {animal}, saiu correndo para avisar seu marido, que trabalhava no(na){lugar_marido}. Ao chegar lá, estava sem fôlego, e precisou de alguns minutos para conseguir explicar a história ao Sr.{nome_homem}. Assim que ouviu, sua reação foi instantânea! Abriu o(a) seu(sua) {lugar_pegou_coisa} e pegou uma {arma_ferramenta} para caçar e matar o animal. Procurou pela casa inteira e até mesmo no(na) {lugar_busca}, mas não conseguia encontrá-lo(a). Finalmente, quando estava quase desistindo, avistou-o(a) no(na) {lugar_animal_estava}. Quando estava prestes a pegá-lo(a), teve uma surpresa, o ser tinha {numero} filhotes, e só saiu para alimentá-los. Entendendo a razão de todo aquele furduncio, colocou a sua {arma_ferramenta} no chão e voltou para {lugar_voltou}, onde encotrou sua esposa {estado}, e explicou a situação toda a ela."

print(madlib)
