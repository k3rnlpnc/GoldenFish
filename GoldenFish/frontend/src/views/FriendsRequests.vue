<template>
    <div class="content">
        <div class="friends-request-list">
            <form method="POST" class="friends-request-form">
                <div class="friend-info">
                    <input name="user_id" type="hidden" value="user_id">
                    <span class="username">Username</span>
                    <span class="fullname">Иван Иванов</span>
                </div>
                <div class="request-buttons">
                    <button type="submit" name="acсept-request"><img src="../assets/img/checkmark.png"></button>
                    <button type="submit" name="delete-request"><img src="../assets/img/delete.png"></button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
export default {
    
}
</script>

<style scoped>
.friends-request-list {
    display: flex;
    justify-content: start;
    flex-wrap: wrap;
    margin: 0 30px;
}

.friends-request-form {
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

.request-buttons {
    background: #ECE3E3;
    margin-left: 2px;
    display: flex;
    align-items: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.request-buttons button {
    background: inherit;
    border: 0;
}

.request-buttons button img {
    width: 18px;
    cursor: pointer;
    padding-top: 5px;
}
</style>