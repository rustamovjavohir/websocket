import json
from channels.generic.websocket import WebsocketConsumer, JsonWebsocketConsumer
from asgiref.sync import async_to_sync


class ChatConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_group_name = None

    def connect(self):
        self.room_group_name = 'test'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        print(f"Channel name: {self.channel_name}")

        self.accept()

        # self.send(text_data=json.dumps({
        #     'type': 'connection_established',
        #     'message': 'Connection established'
        # }))

    # def disconnect(self, close_code):
    #     pass

    def receive(self, text_data: str):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # print('message: ', message)
        # self.send(text_data=json.dumps({
        #     'type': 'chat',
        #     'message': message
        # }))

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def chat_message(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message
        }))


class ChatConsumer2(ChatConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))


class ChatJsonWebsocketConsumer(JsonWebsocketConsumer):
    def connect(self):
        self.room_group_name = 'test'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        # print(f"Channel name: {self.channel_name}")

        self.accept()

        # self.send_json({
        #     'type': 'connection_established',
        #     'message': 'Connection established'
        # })

    def receive_json(self, content, **kwargs):
        message = content['message']

        # print('message: ', message)
        # self.send_json({
        #     'type': 'chat',
        #     'message': message
        # })

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def chat_message(self, event):
        message = event['message']

        self.send_json({
            'type': 'chat',
            'message': message
        })
