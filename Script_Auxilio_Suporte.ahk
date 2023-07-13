#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

gera_senha(){
;gera a senha diária para login no sistema com as credenciais internas
	FormatTime, data, ,ddMM
	hoje_array := StrSplit(data)
		/*
		MsgBox % hoje_array[4] ;final mes
		MsgBox % hoje_array[3] ;comeco mes
		MsgBox % hoje_array[2] ;final dia
		MsgBox % hoje_array[1] ;comeco dia
		*/
	dv1 := (hoje_array[2] - hoje_array[4])*5
		if(strlen(dv1)>1){
		dv1_temp := StrSplit(dv1)
		dv1 := dv1_temp[2]
	}
	dv2 := (hoje_array[1] * hoje_array [2] + dv3)
		if(strlen(dv2)>1){
		dv2_temp := StrSplit(dv2)
		dv2 := dv2_temp[2]
	}
	dv3 := (dv1 + dv2)
		if(strlen(dv3)>1){
		dv3_temp := StrSplit(dv3)
		dv3 := dv3_temp[2]
	}
	dv4 := hoje_array[1] + hoje_array [4]
		if(strlen(dv4)>1){
		dv4_temp := StrSplit(dv4)
		dv4 := dv4_temp[2]
	}
	return dv1 . dv2 . dv3 . dv4
}

^1:: ;digita automaticamente senha interna
Send, senhainterna1
return

^2::
Send, senhainterna2
return

^3:: ;inicia atendimento com bom dia  ou boa tarde dependendo da hora do sistema(am/pm)
FormatTime, periodo, ,tt
if (periodo == AM){
	Send, Bom dia. Em que posso ajudar?
}
else{
	Send, Boa tarde. Em que posso ajudar?
}
return

^4:: ;encerra atendimento com bom final de semana, bom dia ou boa tarde dependendo da data e hora do sistema
FormatTime, dia, ,ddd
FormatTime, periodo, ,tt
if (dia == Sex || dia == Sab){
	Send, Disponha. Tenha um ótimo final de semana. Estou desconectando.
}
else if (periodo == AM){
	Send, Disponha. Tenha um ótimo dia. Estou desconectando.
}
else{
	Send, Disponha. Tenha uma ótima tarde. Estou desconectando
}
return

^Numpad5:: ;abre a tela "run" do windows para utilizar os outros comandos
Send, #r
return

^Numpad1:: ;conecta em um anydesk a partir do run com o número do buffer da área de transferência
Send, C:\Program Files (x86)\AnyDesk\AnyDesk.exe ^v
return

^Numpad2:: ;duplica um arquivo e automaticamente deixa ele em modo de edição de nome
Send, ^c ^v {F2}
return

^5:: ;faz login no sistema com as credenciais internas de administrador
Send, nome_usuário{tab}
senha := gera_senha()
Send, %senha%{enter}
return

^p::
Send, Chrome http://localhost:8080/phpmyadmin/
return

^o::
Send, Chrome http://localhost:8080/doc_supremo/
return

^Numpad6:: ;abre o reindexador de tabelas paradox
Send, C:\...\pdxrbld.exe
return

^+Numpad6:: ;roda o reindexador de tabelas paradox diretamente do run com a configuração mais comum
Send, Pdxrbld /A $imples -R1 -P+ -Q+
return

^Numpad7:: ;abre as pastas com os xml das NFe/NFCe/CTe/MDFe do cliente
Send, C:\...\nome_erp\Web\sistema\www\nome_erp\arquivos_clientes
return

^Numpad8:: ;abre a pasta das tabelas paradox do cliente
Send, C:\...\nome_erp\Dados
return

^Numpad9:: ;abre as tabelas do sistema web do cliente
Send, C:\...\nome_erp\Web\Sistema\base
return