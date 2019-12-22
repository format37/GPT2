lex_source='The search for extraterrestrial civilizations completely failed'
with open("logs/predictions_1.5B.txt",'r') as lex_file:
	lex_result=lex_file.read()
lex_result=lex_result.replace('======================================== SAMPLE 0 ========================================', '')
lex_result=lex_result.replace('================================================================================', '')
lex_result=lex_result.replace(lex_source, '')
#lex_result=lex_result.replace('@gpt2robot', '')
#lex_result='.'.join(lex_result.split('.')[:3])+'.' #crop left 4 sentences
lex_result=lex_result.replace('<|endoftext|>', '')
lex_result=lex_result.replace('\n\n', '\n')
splitter=1
lex_result_new=''
while len(lex_result_new)<300:
	lex_result_new=''.join(lex_result.split('.\n')[1:splitter])
	splitter+=1
	if splitter>100:
		break
lex_result=lex_result_new
print(lex_result)