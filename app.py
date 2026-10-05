import socketio
from aiohttp import web

# Cria instância de servidor assíncrono com cors permitido pra todas as origens.
sio = socketio.AsyncServer(cors_allowed_origins='*')
# Cria aplicação para gerenciar rotas e requisições HTTP.
app = web.Application()
# Vincula(attach) o servidor à aplicação web.
sio.attach(app)

# Função assíncrona que será executada toda vez que a rota receber um acesso
async def handle_update(request):
    # Emite em tempo real um aviso para todos os clientes que estiverem conectados no servidor.
    await sio.emit('atualizar_tela')
    return web.Response(text="Notificado com sucesso", status=200)

# Registrando rota no servidor
app.router.add_post('/notificar', handle_update)

if __name__ == '__main__':
    # Subindo servidor para comunicação em rede local (on-premises)
    web.run_app(app, host='0.0.0.0', port=8532)