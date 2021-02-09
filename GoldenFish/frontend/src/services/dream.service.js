import { instance } from "./api";

class DreamService {
    getMyWishes() {
        return instance.get('mywishes');
    }

    getWishInfo(id) {
        return instance.get('mywishes/' + id);//, { dream_id: id });
    }

    getFriendWish(dreamId) {
        return instance.get('friends/dreams/' + dreamId); //, { dream_id: dream_id });
    }

    addWish(wish) {
        return instance.post('mywishes', {
            name: wish.name,
            description: wish.description,
            store_link: wish.store_link,
            image_link: wish.image_link,
            is_fulfilled: false
        });
    }

    deleteWish(id) {
        return instance.delete('mywishes/' + id);
    }

    editWish(wish) {
        return instance.put('mywishes/' + wish.id, {
            name: wish.name,
            description: wish.description,
            store_link: wish.store_link,
            image_link: wish.image_link,
        });
    }

    setWishFulfilled(id) {
        return instance.put('mywishes/' + id, { is_fulfilled: true });
    }

    getFulfilledWishes() {
        return instance.get('fulfilled');
    }
}

export default new DreamService();