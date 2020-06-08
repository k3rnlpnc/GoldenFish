<template>
    <div class="content">
        <div class="wishes">
            <div class="wish-line">
                <div class="wish-info">
                    <div class="wish-info-line">
                        <span class="wish-name">Подарок1</span>
                        <span class="friend-name">friend1</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    
}
</script>

<style scoped>
.wishes {
    margin: 50px;
}

.wish-line {
    width: inherit;
    height: 40px;
    display: flex;
    margin-bottom: 10px;
}

.wish-info {
    background: #ECE3E3;
    width: 100%;
    font-size: 20px;
    line-height: 20px;
    color: #000000;
    padding: 10px 25px;
}

.wish-info-line {
    display: flex;
    justify-content: space-between;
    border-bottom: 1px solid #E1DADA;
}
</style>