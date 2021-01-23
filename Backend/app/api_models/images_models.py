from app.views import images_api_call
from flask_restx import fields

new_category_model = images_api_call.model("New Category", {
    "category_name":fields.String("category_name"),
})

new_images_model = images_api_call.model("New Image", {
    "image_title":fields.String("image_title"),
    "image_tag":fields.String("image_tag"),
    "img_local_url":fields.String("img_local_url"),
    "cloudinary_url":fields.String("cloudinary_url"),
    "category_id":fields.String("category_id"),
})