<template>

  <body>

    <div>
        <div class="container">
          <div class="row justify-content-center align-items-center">
            <div class="col-md-6">
              <div class="row">
                <div class="col-xl-12">
                    <h4 class="text-center mb-4">User Registration</h4>
                    <form @submit.prevent="register" method="post">
                        <div class="form-group">
                            <label><strong>Username</strong></label>
                            <input type="text" class="form-control" v-model="username">
                        </div>
                        <div class="form-group">
                            <label><strong>Password</strong></label>
                            <input type="password" class="form-control" v-model="password">
                        </div>
                        <div class="text-center">
                            <button type="submit" class="btn btn-primary btn-block">Register</button><br>

                            <nuxt-link to="login">
                              <span>Already has an account? Login</span>
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

      async register(){

          try{

            var data = {
              username:this.username,
              password:this.password
            };

            let res = await this.$store.dispatch("account/registerUser", data);

            this.$swal("", "Registraion successful proceed to login");
              
          }
          catch(error){
              console.log(error.response);
              this.$swal("",'Something went wrong try again !!!', "error");
          }

      }

  }
  

}
</script>


