# elo7Challenge

**Este arquivo contém a solução para o Teste de Programação para a Vaga de Estagiário da elo7**</br>
O Aplicativo final pode ser encontrado em: https://andre-elo7challenge.herokuapp.com/ </br>

Para a resolução, optei pela utilização da linguagem *Python* com o framework *Django* para desenvolvimento Web. Escolhi python pois já tinha feito um exercício parecido (uma agenda de contatos) em JavaWeb e como nunca tinha trabalhado com *Django* antes. Então, achei que seria uma ótima opotunidade para aprender. Além disso, python oferece algumas facilidades para aplicação de algumas estatísticas e eu já tinha trabalhado com o uso da API do Twitter utilizando python no passado. </br>

Fiz uso de algumas bibliotecas pois como não havia nenhuma restrição na especificação, quis deixar o código o mais limpo e organizável possível. </br>

Resolvi focar apenas na parte que a especificação exigia. Dado que o exercício é para o time de *Data Science*, resolvi não focar em *frontend* e por isso a parte de front da aplicação é basicamente HTML. </br>

Caso deseje rodar a aplicação localmente, siga os seguintes passos:
* clone o repositório
* entre na pasta `challenge`
* altere o arquivo `settings.py` de forma que ele conecte-se a um banco local (como o sqlite3)
* execute `pip install -r requirements.txt`, perferencialmente dentro de um `virtualenv`
* execute `python manage.py runserver`
