const apiEndPoints = {

    'addImage': '/images/add',
    'filterImage':'/images/filter-images',
    'fetchCategories':'/images/fetch-categories',
    'addCategory':'/images/new-category'

}

export const state = () => ({

})

export const actions = {

    async addImage({state, commit}, data){

        let res = await this.$axios.post(apiEndPoints.addImage, data);

        return res
    },

    async addCategory({state, commit}, data){

        let res = await this.$axios.post(apiEndPoints.addCategory, data);

        return res
    },

    async filterImage({state, commit}, data){

        let res = await this.$axios.get(apiEndPoints.filterImage + "?by_category_name="+data["by_category_name"] + "&by_tag_name="+data["by_tag_name"]);

        return res;
        
    },

    async fetchCategories({state, commit}){

        let res = await this.$axios.get(apiEndPoints.fetchCategories);

        return res;
    }

}