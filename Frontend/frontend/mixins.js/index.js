export default{

    data() {
        return {
          all_categories: [],
          all_images:[],
          //ADD IMAGES
          image_title: "",
          image_tag: "",
          category_id: "",
          //ADD CATEGORIES
          category_name:"",
        };
      },
    
      methods: {
        async addImage() {
          try {
            var fd = new FormData();
    
            var push_to_cloud = document.getElementById("should_upload_to_cloud").checked;
    
            fd.append("image_title", this.image_title);
            fd.append("image_tag", this.image_tag);
            fd.append("category_id", this.category_id);
            fd.append("upload_to_cloudinary", push_to_cloud);
            fd.append("file", document.getElementById("img_url").files[0]);
    
            let res = await this.$store.dispatch("addImage", fd);
            this.$swal("", "Image Successfully Added !!!", "success");
    
            this.$fetch();
            $("#addImageModal .close").click();
            
          } catch (error) {
    
            console.log(error.response);
            this.$swal("", "Something went wrong try again !!!", "error");
    
          }
        },
        async addCategory() {
          try {
    
            var data = {
              "category_name":this.category_name,
            };
    
            let res = await this.$store.dispatch("addCategory", data);
            this.$swal("", "Category Successfully Added !!!", "success");
    
            this.$fetch();
            $("#addCategoryModal .close").click();
    
          } catch (error) {
            alert(error.message);
            // console.log(error.response);
            // this.$swal("", "Something went wrong try again !!!", "error");
          }
        },
        
        async filterCategory() {
          try {
    
            var c_id = document.getElementById("filter_category_id").value;
    
            var data = {
              by_category_name:c_id,
              by_tag_name: ""
            };
            
            let res = await this.$store.dispatch("filterImage", data);
            this.all_images = res.data.message;
    
            let category_res = await this.$store.dispatch("fetchCategories");
            this.all_categories = category_res.data.message;
    
            
          } catch (error) {
            console.log(error.response);
            alert(error.message);
            // this.$swal("", "Something went wrong try again !!!", "error");
          }
        },
    
        async searchCategory() {
            
          try {
    
            var tag_name = document.getElementById("search_tag_name").value;
    
            var data = {
              by_category_name:"",
              by_tag_name: tag_name
            };
            
            let res = await this.$store.dispatch("filterImage", data);
            this.all_images = res.data.message;
    
            let category_res = await this.$store.dispatch("fetchCategories");
            this.all_categories = category_res.data.message;
    
            
          } catch (error) {
            console.log(error.response);
            alert(error.message);
            // this.$swal("", "Something went wrong try again !!!", "error");
          }
        },
        
      },
    

}