export default class Dream {
    constructor(id, owner_id, name, description, image_link, store_link, is_fulfilled) {
      this.id = id;
      this.owner_id = owner_id;
      this.name = name;
      this.description = description;
      this.image_link = image_link;
      this.store_link = store_link;
      this.is_fulfilled = is_fulfilled;
    }
  }