import { instance } from "./api";

class GiftService {
    getGifts() {
        return instance.get('gifts');
    }

    addGift(friendId, dreamId) {
        return instance.put('friends/'+ friendId + '/' + dreamId, {
            friend_id: friendId,
            dream_id: dreamId
        });
    }

    deleteGift(id) {
        return instance.delete('gifts/' + id);
    }
}

export default new GiftService();