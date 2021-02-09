import { instance } from "./api";

class FriendService {
    getFriends() {
        return instance.get('friends');
    }

    getFriendRequests() {
        return instance.get('friends/requests');
    }

    addFriend(id) {
        return instance.put('users/' + id, { user_id: id });
    }

    deleteFriend(id) {
        return instance.delete('friends/' + id);
    }

    acceptRequest(senderId) {
        return instance.put('friends/requests/' + senderId, { sender_id: senderId });
    }

    rejectRequest(senderId) {
        return instance.delete('friends/requests/' + senderId);
    }

    getFriendWishes(id) {
        return instance.get('friends/' + id, { friend_id: id });
    }
}

export default new FriendService();