const apiEndPoints = {

    'register': '/users/register'

}

export const state = () => ({

})

export const actions = {

    async registerUser({state, commit}, data){

        let res = await this.$axios.post(apiEndPoints.register, data)

        return res
    }

}