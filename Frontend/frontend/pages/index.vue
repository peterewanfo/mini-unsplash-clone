<template>
  <div>
    <div class="container" style="margin-top:20px;">
      <div class="row">
        <div class="col-sm-6">
          <div>
            <h4>Hi, welcome!</h4>
            <span>Mini Unsplash Platform</span>

            <button
              data-toggle="modal"
              data-target="#addImageModal"
              class="btn btn-success"
            >
              Add Image
            </button>
            <button
              data-toggle="modal"
              data-target="#addCategoryModal"
              class="btn btn-success"
            >
              Add Category
            </button>
          </div>
        </div>

        <div class="modal" id="addImageModal">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title">Add Image</h5>
                <button type="button" class="close" data-dismiss="modal">
                  <span>&times;</span>
                </button>
              </div>
              

              <form @submit.prevent="addImage" method="post">
                <div class="modal-body">
                  <div class="form-row">
                    <div class="form-group col-md-12">
                      <label>Image Title</label>
                      <input v-model="image_title" type="text" class="form-control" placeholder="" />
                    </div>

                    <div class="form-group col-md-12">
                      <label>Image Tag</label>
                      <input v-model="image_tag" type="text" class="form-control" placeholder="" />
                    </div>

                    <div class="form-group col-md-12">
                      <label>Select Category</label>
                      <select v-model="category_id" class="form-control col-md-12">
                        <option :value="`${category.id}`" v-for="category in this.all_categories" :key="category.id">{{ category.category_name }}</option>
                      </select>
                    </div>

                    <input
                      placeholder="Photo URL"
                      type="file"
                      id="img_url"
                      class="form-control"
                    /><br><br>

                    <center>
                      <label>UPLOAD TO CLOUDINARY</label>
                    </center>
                    
                    <input type="checkbox" style="width:25px;height:25px;margin-left:15px;" id="should_upload_to_cloud"/><br>

                    <span style="color:red;"> When upload to cloudinary is enabled, there may be a little delay in upload due to time cloudinary... A faster means would be to upload on background through celery.. </span>

                  </div>
                </div>
                <div class="modal-footer">
                  <button
                    type="button"
                    class="btn btn-danger light"
                    data-dismiss="modal"
                  >
                    Close
                  </button>
                  <button type="submit" class="btn btn-primary">
                    Add Image
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>

        <div class="modal" id="addCategoryModal">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title">Add Category</h5>
                <button type="button" class="close" data-dismiss="modal">
                  <span>&times;</span>
                </button>
              </div>

              <form @submit.prevent="addCategory" method="post">
                <div class="modal-body">
                  <div class="form-row">
                    <div class="form-group col-md-12">
                      <label>Category Name</label>
                      <input type="text" v-model="category_name" class="form-control" placeholder="" />
                    </div>

                  </div>
                </div>
                <div class="modal-footer">

                  <button
                    type="button"
                    class="btn btn-danger light"
                    data-dismiss="modal"
                  >
                    Close
                  </button>

                  <button type="submit" class="btn btn-primary">
                    Add Category
                  </button>

                </div>
              </form>
            </div>
          </div>
        </div>

        <div class="col-sm-6">
          <nuxt-link to="/logout">
            <button class="btn btn-danger float-right">LOGOUT</button>
          </nuxt-link>
        </div>
      </div><br>

      <div
        class="row col-md-6"
        style="margin: 0 auto !important; width: 60%; margin-bottom:8px;"
      >
        <input class="form-control col-md-8" placeholder="Search Image By" id="search_tag_name" />

        <div class="col-md-2">
          <button class="btn btn-info float-right" type="button" @click="searchCategory()">SEARCH</button>
        </div>
      </div>

      <center>
        <span>Filter By Category:</span>
      </center>

      <div class="row col-md-6" style="margin: 0 auto !important; width: auto;">
        <select class="form-control col-md-8" id="filter_category_id">

          <option :value="`${category.id}`" v-for="category in this.all_categories" :key="category.id">{{ category.category_name }}</option>

        </select>

        <div class="col-md-2">
          <button class="btn btn-info" type="button" @click="filterCategory()" style="margin-left:5px;" id="btn_filter">Filter</button>
        </div>
      </div>
      <br />

      <div class="row">
        <div class="col-xl-2 col-lg-3 col-md-2 col-sm-6 image-wrapper" v-for="image in all_images" :key="image.id">
          <center>
            <div>
              <img data-toggle="modal" :data-target="`#viewImageModal_${image.id}`" class="image" style="" :src="`${image.img_local_url}`" alt="" />
            </div>
            
          </center>

          <div class="modal" :id="`#viewImageModal_${image.id}`">
          <div class="modal-dialog">
            <div class="modal-content">
              <img class="image" style="" width="200px;" height="200px" :src="`${image.img_local_url}`" alt="" />
            </div>
          </div>
        </div>

        </div>

      </div>
    </div>
  </div>
</template>

<script>

import IndexMixin from '~/mixins.js/index.js';

export default {

  middleware: "auth",
  
  mixins: [IndexMixin],

  async fetch() {

    let category_res = await this.$store.dispatch("fetchCategories");
    this.all_categories = category_res.data.message;

    var data = {
      by_category_name:"",
      by_tag_name: ""
    }
    
    let res = await this.$store.dispatch("filterImage", data);

    this.all_images = res.data.message;

  }
};
</script>

<style scoped>
a {
  color: #000;
}

.image-wrapper {
  padding-left: 5px !important;
  padding-right: 5px !important;
}

.image {
  border-radius: 18px;
  background-color: red;
  width: 100%;
  height: 250px;
  margin-bottom: 8px;
}
</style>
