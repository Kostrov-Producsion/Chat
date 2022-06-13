<template>
  <div id="app">
    <Nav
       v-bind:count_possible="count_possible"
       v-bind:unread_chats="unread_chats"
       v-bind:is_valid="is_valid"
       v-bind:selected-nav-mobile="funcSelectedNav"
       v-bind:changeAuth="changeAuth"
       @getOut="getOut"
    />
    <div v-if="is_valid">
      <BaseContent
            v-bind:get-cookie="getCookie"
            @incoming="Incoming"
            @WebSocketClose="closeWS"
            @funcSelectedNav="funcSelectedNav=$event"
            @getOut="getOut"
      />
    </div>
    <div v-else>
      <div v-if="is_auth">
        <Authorization
                v-bind:success_reg="success_reg"
                v-bind:change_password="change_password"
                @authorization="AuthHandler"
        />
      </div>
      <div v-else>
        <div v-if="is_password">
          <PasswordRecovery
             v-bind:get-cookie="getCookie"
             @password_recovery="Auth"
          />
        </div>
        <div v-else>
          <Registration
              v-bind:get-cookie="getCookie"
              @registration="Auth"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import BaseContent from './views/BaseContent';
  import Authorization from './views/Authorization';
  import Registration from './views/Registration';
  import PasswordRecovery from "./views/PasswordRecovery";
  import Nav from './views/Nav'

  import axios from 'axios';

  export default {
      data: function () {
        return {
          api_token: 'Kostrov 888',
          is_valid: false,
          is_auth: true,
          is_password: false,
          success_reg: false,
          change_password: false,
          count_possible: null,
          unread_chats: null,
          wsPhotoSetting: null,
          wsSetting: null,
          wsPhotoMessage: null,
          wsVideo: null,
          wsMessages: null,
          wsChat: null,
          wsFriendAdd: null,
          wsConnect: null,
          wsPerson: null,
          funcSelectedNav: Function
        }
    },
    components: {PasswordRecovery, BaseContent, Nav, Authorization, Registration },
    created() {
        this.ActivateStyle();
    },
    mounted: function () {
      if (localStorage.getItem('authToken')) {
        this.api_token = localStorage.getItem('authToken')
      }
      axios.post(
        `${this.$store.getters.getServerUrl}/api/token/verify/`,
        {
          token: this.api_token.match(/Kostrov\s(.+)/)[1]
        }
      ).then(response => (this.is_valid = true)
      ).catch(error => console.log(error));
    },
    methods: {
      AuthHandler (auth) {
          this.is_valid = auth;
          this.success_reg = false;
          this.change_password = false;
      },
      changeAuth (event) {
        var target = event.target.closest('a');
        var action = target.getAttribute('data-auth');
        if (action === 'registration') {
          this.is_auth = false;
          this.is_password = false;
        } else if (action === 'authorization') {
          this.is_auth = true;
          this.is_password = false;
        } else if (action === 'password') {
          this.is_auth = false;
          this.is_password = true;
        }
      },
      Auth (user) {
        if (this.is_password) {
          this.is_auth = user;
          this.change_password = user;
        } else {
          this.is_auth = user;
          this.success_reg = user;
        }
      },
      Incoming (data) {
        this.unread_chats = data.unread_chats;
        this.count_possible = data.count_possible;
      },
      closeWS (data) {
        this.wsMessages = data.wsMessages;
        this.wsChat = data.wsChat;
        this.wsFriendAdd = data.wsFriendAdd;
        this.wsConnect = data.wsConnect;
        this.wsPerson = data.wsPerson;
        this.wsPhotoSetting = data.wsPhotoSetting;
        this.wsSetting = data.wsSetting;
        this.wsPhotoMessage = data.wsPhotoMessage;
        this.wsVideo = data.wsVideo;
      },
      getOut(data) {
        this.is_valid = data;
        this.wsPhotoSetting.close();
        this.wsSetting.close();
        this.wsPhotoMessage.close();
        this.wsVideo.close();
        this.wsMessages.close();
        this.wsChat.close();
        this.wsFriendAdd.close();
        this.wsConnect.close();
        this.wsPerson.close();
      },
      ActivateStyle() {
        var style = parseInt(this.getCookie());
        if (style === 1) {
            document.body.classList.add('night')
        } else if (style === 2) {
            document.body.classList.add('warm')
        } else {
            document.body.removeAttribute('class');
        }
      },
      getCookie() {
          var data = document.cookie.match(/style=(\d)/);
          if (data) {
            return data[1]
          } else {
            return 0
          }
      }
    }
  }
</script>
