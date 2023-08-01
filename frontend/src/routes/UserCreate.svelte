<script>
    import {push} from 'svelte-spa-router'
    import {create_user} from '../lib/api';

    let username = ''
    let password1 = ''
    let password2 = ''
    let email = ''
    let birthday = ''

    let error = []

    async function fast_create_user(event){
        event.preventDefault()

        const _body = {
            "username" : username,
            "password1" : password1,
            "password2" : password2,
            "email" : email,
            "birthday" : birthday
        }

        const result = await create_user(_body) 

        if (result[0]){
            push('/')
        }else {
            error = result[1]
            //console.log(error)        
        }

    }
    
</script>

<div class="container">
    <h5 class="my-3 border-bottom pb-2">회원 가입</h5>
    <form method="post">
        <div class="mb-3">
            <label for="username">사용자 이름</label>
            <input type="text" class="form-control" id="username" bind:value="{username}">
        </div>
        <div class="mb-3">
            <label for="password1">비밀번호</label>
            <input type="password" class="form-control" id="password1" bind:value="{password1}">
        </div>
        <div class="mb-3">
            <label for="password2">비밀번호 확인</label>
            <input type="password" class="form-control" id="password2" bind:value="{password2}">
        </div>
        <div class="mb-3">
            <label for="email">이메일</label>
            <input type="text" class="form-control" id="email" bind:value="{email}">
        </div>
        <div class="mb-3">
            <label for="birthday">생일</label>
            <input type="text" class="form-control" id="birdhday" bind:value="{birthday}">
        </div>
        <button type="submit" class="btn btn-primary" on:click={(response) => fast_create_user(response)}>생성하기</button>
    </form>
    <div>
        {#each error as er}
            <li>{er}</li>
        {/each}
    </div>
</div>