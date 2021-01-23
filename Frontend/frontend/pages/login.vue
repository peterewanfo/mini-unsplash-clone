<template>

  <body>

    <div>
        <div class="container">
          <div class="row justify-content-center align-items-center">
            <div class="col-md-6">
              <div class="row">
                <div class="col-xl-12">
                    <h4 class="text-center mb-4">User Login</h4>
                    <form novalidate @submit.prevent="login" method="post">
                        <div class="form-group">
                            <label><strong>Username</strong></label>
                            <input type="text" class="form-control" v-model="username">
                        </div>
                        <div class="form-group">
                            <label><strong>Password</strong></label>
                            <input type="password" class="form-control" v-model="password">
                        </div>
                        <div class="text-center">
                            <button type="submit" class="btn btn-primary btn-block">Login</button><br>

                            <nuxt-link to="registration">
                              <span>Register User</span>
                            </nuxt-link>

                        </div>
                    </form>
                </div>
              </div>
            </div>
          </div>

          

        </div>
    </div>

  </body>

</template>

<script>
export default {

  layout: "login_default",
  middleware: "guest",

  data() {

    return {
      username: "",
      password: ""

    }

  },

  methods: {

      async login(){

          try{

              let res = await this.$auth.loginWith('local', {
                  data : {
                      username: this.username,
                      password: this.password
                  }
              })

              if (this.$auth.loggedIn) {
                  this.$router.go('/');
              }
              
          }
          catch(error){
              console.log(error.response);
              this.$swal("",'Wrong Login Credentials !!!', "error");
          }

      }

  }
  

}
</script>


