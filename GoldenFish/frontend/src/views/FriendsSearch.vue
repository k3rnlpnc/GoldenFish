<template>
    <div class="container">
        <h3 class="search-title">Результат поиска</h3>
        <p class="no-result">Поиск не дал резульатов. Измените параметры поиска.</p>
        <div class="result">
            <form method="POST" class="add-friend-form">
                <div class="user-info">
                    <input name="user_id" type="hidden" value="user_id">
                    <span class="username">Username</span>
                    <span class="fullname">Иван Иванов</span>
                </div>
                <div class="add-friend-button">
                    <button type="submit"><img src="../assets/img/checkmark.png"></button>
                </div>
            </form>
        </div>
        <hr class="end-line">
    </div>
</template>

<script>
export default {
    
}
</script>

<style scoped>
.search-title {
    text-align: center;
    margin: 80px 80px 40px 80px;
    font-size: 30px;
    line-height: 35px;
    color: #6C3F5E;;
}

.no-result {
    font-size: 25px;
    text-align: center;
    display: none;
}

.result {
    display: flex;
    flex-wrap: wrap;
    margin: 0 30px;
}

.add-friend-form {
    padding: 15px;
    display: flex;
    flex-direction: row;
}

.user-info {
    background: #ECE3E3;
    height: 60px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 10px 20px;
}

.user-info .username {
    font-size: 25px;;
}

.user-info .fullname {
    font-size: 20px;
}

.add-friend-button {
    background: #ECE3E3;
    margin-left: 2px;
    display: flex;
    align-items: center;
}

.add-friend-button button {
    background: inherit;
    border: 0;
}

.add-friend-button button img {
    width: 18px;
    height: 18px;
    cursor: pointer;
}

.end-line {
    color: (140, 102, 128, 0.5);
    margin: 0 30px;
}
</style>