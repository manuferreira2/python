import pymysql

conexao = pymysql.connect(host='localhost',
                          database='meubd',
                          user='root',
                          password='senha')
cursor = conexao.cursor()

sql = f"select CPF,TELEFONE from meubd.baseclientestotal where dt_atualizacao is null"

cursor.execute(sql)
resultado = cursor.fetchall()

for c in resultado:
    cpf = c[0]
    telefone = str(c[1])
    ddd = telefone[:2]
    tel = telefone[2:]
    pn = telefone[2:3]

    if len(tel) < 8:
        'telefone invalido'
        sql = f"update meubd.baseclientestotal set dt_atualizacao = now(),TELEFONE = null where cpf = {cpf} and TELEFONE = {telefone}"
        cursor.execute(sql)
        conexao.commit()

    elif (pn == '7' or pn == '8' or pn == '9') and len(tel) == 8:
        #print('celular - falta 9° digito')
        tel = '9'+tel
        sql = f"update meubd.baseclientestotal set dt_atualizacao = now(),TELEFONE = {ddd+tel} where cpf = {cpf} and TELEFONE = {telefone}"
        cursor.execute(sql)
        conexao.commit()
       
    else:
        #nenhuma alteração para ser realizada
        print('telefone ok')
