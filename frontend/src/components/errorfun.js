const Error = (subject, content) => {

    let errors_check = {subject: '', content: ''}
    let valid = false

    if (subject.trim().length < 5) {
        valid = true
        errors_check.subject = '제목은 최소 5글자 이상이여야 합니다.'
    }
    if (content.trim().length < 1) {
        valid = true
        errors_check.content = '내용을 작성해주세요.'
    } 

    return {valid, errors_check}
};

export default Error;