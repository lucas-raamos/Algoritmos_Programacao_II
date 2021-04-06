from AP_aula05.conta import conta

c1 = conta()
c1.imprimirSaldo()

c1.depositar( 10.50 )
c1.imprimirSaldo()

c1.sacar( 5.2 )
c1.imprimirSaldo()

c1.__saldo = 20
c1.imprimirSaldo()