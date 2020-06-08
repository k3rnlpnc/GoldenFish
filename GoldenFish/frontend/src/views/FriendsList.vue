<template>
    <div class="content">
        <form method="POST" class="delete-friend-form">
            <div class="friend-info">
                <input name="user_id" type="hidden" value="user_id">
                <span class="username">Username</span>
                <span class="fullname">Иван Иванов</span>
            </div>
            <div class="delete-friend-button">
                <button type="submit" name="delete-friend"><img src="../assets/img/delete.png"></button>
            </div>
        </form>
    </div>
</template>

<script>
export default {
    
}
</script>

<style scoped>
.friends-list {
    display: flex;
    justify-content: start;
    flex-wrap: wrap;
    margin: 0 30px;
}

.delete-friend-form {
    padding: 15px;
    display: flex;
    flex-direction: row;
}

.friend-info {
    background: #ECE3E3;
    height: 60px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 10px 20px;
}

.friend-info .username {
    font-size: 25px;;
}

.friend-info .fullname {
    font-size: 20px;
}

.delete-friend-button {
    background: #ECE3E3;
    margin-left: 2px;
    display: flex;
    align-items: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.delete-friend-button button{
    background: inherit;
    border: 0;
}

.delete-friend-button button img{
    width: 18px;
    cursor: pointer;
    padding-top: 5px;
}
</style>