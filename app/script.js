function is_correct(password) {
    // 비밀번호 길이가 8 ~ 16자가 아닌 경우
    if(!(8 <= password.length && password.length <= 16)) {
        return false;
    }

    // 숫자, 특수문자, 영문 대소문자가 아닌 경우
    const regex = /^[a-zA-Z0-9`~!@#$%^&*()-_=+\[{\]}\\|;:'",./?]+$/;
    if(!regex.test(password)) {
        return false;
    }

    return true;
}

function standardScaling(X, mean, scale) {
    return X.sub(mean).div(scale);
}

function showResult(prediction) {
    if(prediction < 0.5) {
        document.getElementById('checkImage').src = 'imgs/lock.png'; // 안전한 비밀번호
    } else {
        document.getElementById('checkImage').src = 'imgs/unlock.png'; // 취약한 비밀번호
    }

    const p = prediction*100;
    document.getElementById('percentageText').textContent = "해킹 위험률: "+p.toFixed(2)+"%";
}

async function runModel(feature, mean, scale) {
    // 모델 불러오기
    const model = await tf.loadLayersModel('model.json');

    // 텐서로 변환
    var X = tf.tensor2d([feature])
    mean = tf.tensor(mean);
    scale = tf.tensor(scale);

    // 정규화
    X = standardScaling(X, mean, scale);

    // 모델 예측
    const Y = model.predict(X);

    // 결과 반환
    showResult(Y.arraySync()[0][0]);
}

function request(password) {
    $.ajax({
        url: 'password.php',
        type: 'post',
        data: { password: password },
        dataType: 'json',
        success: function(data) {
            const feature = data.feature.trim().split(' ').map(function(x) {
                return parseInt(x);
            });

            const mean = [1.38849431, 0.30185173, 3.30258538, 6.20826606, 1.3450427, 1.63144926, 0.15413074];
            const scale = [3.05560739, 1.79689853, 4.33496041, 4.88338802, 0.55124451, 0.62018868, 0.36107403];

            runModel(feature, mean, scale);
        },
        error: function(error) {
            document.getElementById('checkImage').src = 'imgs/question.png';
            alert("");
        }
    });
}

function checkPassword() {
    var password = document.getElementById('passwordInputText').value;

    if(is_correct(password)) {
        document.getElementById('checkImage').src = 'imgs/loading.png';
        request(password);
    } else {
        document.getElementById('checkImage').src = 'imgs/question.png';
    }
}
