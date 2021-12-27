<template>
  <div class="loginBox">
    <v-container>
      <v-card class="mx-auto rounded-lg" max-width="500" elevation="3">
        <v-card-title>Вход</v-card-title>
        <v-card-text>
          <v-text-field
            class="rounded-lg"
            label="Логин"
            outlined
          ></v-text-field>
          <v-text-field
            class="rounded-lg"
            label="Пароль"
            outlined
          ></v-text-field>
          <v-col>
            <v-row align="center" justify="end">
              <v-btn color="primary" rounded>
                Войти
              </v-btn>
            </v-row>
          </v-col>
        </v-card-text>
      </v-card>
    </v-container>
  </div>
</template>

<script>
export default {
  name: 'Login',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
