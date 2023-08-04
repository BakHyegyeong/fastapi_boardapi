import { writable } from 'svelte/store'

//새로고침해도 변수가 초기화되지 않음.
const persist_storage = (key, initValue) => {
    const storedValueStr = localStorage.getItem(key)
    const store = writable(storedValueStr != null ? JSON.parse(storedValueStr) : initValue)
  
    store.subscribe((val) => {
        localStorage.setItem(key, JSON.stringify(val))
        /*if (val != undefined) {
            localStorage.setItem(key, JSON.stringify(val));
        } else {
            console.log(`Warning: Undefined value detected for key: ${key}`);
        }*/
    })

    return store
}

export const page = persist_storage("page", 0)
//export const page = writable(0)
// 쓰기가능한 스토어 변수 page와 초기값을 0으로 설정.

export const access_token = persist_storage("access_token", "")
export const user_name = persist_storage("user_name", "");
export const is_login = persist_storage("is_login", false)
