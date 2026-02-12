<!doctype html>
<html lang="zh-TW" class="h-full">
 <head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>活動繳費管理系統</title>
  <script src="https://cdn.tailwindcss.com/3.4.17"></script>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
  <style>
    body { box-sizing: border-box; }
    * { font-family: 'Noto Sans TC', sans-serif; }
    .fade-in { animation: fadeIn 0.3s ease-out; }
    @keyframes fadeIn { from { opacity: 0; transform: translateY(-10px); } to { opacity: 1; transform: translateY(0); } }
    .warning-pulse { animation: pulse 2s infinite; }
    @keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.7; } }
    /* Loading Overlay */
    #loading-overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.7); display: flex; justify-content: center; align-items: center; z-index: 100; backdrop-filter: blur(5px); }
  </style>
 </head>
 <body class="h-full bg-gradient-to-br from-emerald-900 via-teal-800 to-cyan-900 overflow-auto">
  
  <div id="loading-overlay" class="hidden">
    <div class="text-white text-xl font-bold flex flex-col items-center">
      <svg class="animate-spin h-10 w-10 text-emerald-400 mb-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
        <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
        <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
      </svg>
      資料同步中...
    </div>
  </div>

  <div id="app-container" class="w-full min-h-full p-4 md:p-8">
   <div class="max-w-6xl mx-auto">
    <header class="text-center mb-8">
     <h1 id="main-title" class="text-3xl md:text-4xl font-bold text-white mb-2">活動繳費管理系統</h1>
     <p id="activity-subtitle" class="text-emerald-200 text-lg">每週四活動</p>
    </header>
    
    <div id="warning-section" class="hidden mb-6 fade-in">
     <div class="bg-amber-500/20 border-2 border-amber-400 rounded-2xl p-4 backdrop-blur-sm">
      <h3 class="text-amber-300 font-bold text-lg mb-3 flex items-center gap-2">
       ⚠️ 繳費提醒名單（剩餘2次以下）</h3>
      <div id="warning-list" class="space-y-2"></div>
     </div>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
     <div class="lg:col-span-1">
      <div class="bg-white/10 backdrop-blur-md rounded-2xl p-6 border border-white/20">
       <h2 class="text-xl font-bold text-white mb-4">➕ 新增/繳費</h2>
       <form id="add-form" class="space-y-4">
        <div><label class="block text-emerald-200 text-sm mb-2">人員名稱</label> <input type="text" id="member-name" placeholder="輸入姓名" class="w-full px-4 py-3 rounded-xl bg-white/10 border border-white/20 text-white placeholder-white/50 focus:outline-none focus:ring-2 focus:ring-emerald-400"></div>
        <div><label class="block text-emerald-200 text-sm mb-2">繳費金額</label>
         <div class="flex items-center gap-2">
           <button type="button" id="decrease-btn" class="w-12 h-12 rounded-xl bg-rose-500/30 text-white font-bold text-2xl">−</button> 
           <input type="number" id="payment-amount" value="100" min="100" step="100" readonly class="flex-1 px-4 py-3 rounded-xl bg-white/10 border border-white/20 text-white text-center text-xl font-bold"> 
           <button type="button" id="increase-btn" class="w-12 h-12 rounded-xl bg-emerald-500/30 text-white font-bold text-2xl">+</button>
         </div>
        </div>
        <div class="bg-white/5 rounded-xl p-4 border border-white/10">
         <div class="flex justify-between text-emerald-200"><span>可參加次數：</span> <span id="sessions-preview" class="font-bold text-white">1 次</span></div>
        </div>
        <button type="submit" id="submit-btn" class="w-full py-3 rounded-xl bg-gradient-to-r from-emerald-500 to-teal-500 text-white font-bold text-lg transition-all hover:scale-[1.02]"> 確認繳費 </button>
       </form>
      </div>
      
      <div class="mt-6 bg-white/10 backdrop-blur-md rounded-2xl p-6 border border-white/20">
       <div class="grid grid-cols-2 gap-4">
        <div class="bg-white/5 rounded-xl p-4 text-center"><p class="text-3xl font-bold text-emerald-400" id="total-members">0</p><p class="text-emerald-200 text-sm">總人數</p></div>
        <div class="bg-white/5 rounded-xl p-4 text-center"><p class="text-3xl font-bold text-amber-400" id="total-revenue">0</p><p class="text-emerald-200 text-sm">總收入</p></div>
       </div>
      </div>
     </div>

     <div class="lg:col-span-2">
      <div class="bg-white/10 backdrop-blur-md rounded-2xl p-6 border border-white/20">
       <h2 class="text-xl font-bold text-white mb-4">📋 參與者名單</h2>
       <div id="members-list" class="space-y-3">
        <div class="text-center py-12 text-emerald-200/50"><p>讀取中...</p></div>
       </div>
      </div>
     </div>
    </div>
   </div>
  </div>

  <div id="delete-modal" class="fixed inset-0 bg-black/50 backdrop-blur-sm hidden items-center justify-center z-50">
   <div class="bg-slate-800 rounded-2xl p-6 m-4 max-w-sm w-full border border-white/20">
    <h3 class="text-xl font-bold text-white mb-2">確認刪除</h3>
    <p class="text-slate-300 mb-6">確定要刪除 <span id="delete-name" class="font-bold text-amber-400"></span> 嗎？</p>
    <div class="flex gap-3"><button id="cancel-delete" class="flex-1 py-2 rounded-xl bg-slate-600 text-white">取消</button> <button id="confirm-delete" class="flex-1 py-2 rounded-xl bg-rose-500 text-white">確認刪除</button></div>
   </div>
  </div>

  <div id="toast-container"></div>

  <script>
    // ==========================================
    // ⚠️ 設定區：請將你的 Google Apps Script 網址貼在下面引號中
    // ==========================================
    const GAS_URL = "https://script.google.com/macros/s/AKfycbyyauu7BqfuV4fTb6V70YIXhJaaF1X7moPgsWWIScUIFX43abR_lsY3T1Lecl86z7V6Fw/exec"; 
    // 例如: "https://script.google.com/macros/s/AKfycbx.../exec"
    
    let membersData = [];
    let pendingDeleteId = null;

    // --- 日期計算邏輯 ---
    function calculateSessions(amount) {
      return Math.floor(amount / 100);
    }

    function getNextThursdays(count, startDateStr) {
      const dates = [];
      // 若無 startDate 則以當下為主，但這裡為了簡化，每次讀取後端資料時重算
      // 正確邏輯：應該依據「最後一次有效日期」往後推，或是依據「繳費當週」往後推
      // 這裡採用簡易邏輯：假設 StartDate 是繳費日
      let baseDate = new Date(startDateStr || new Date()); 
      
      // 調整到下一個週四 (如果今天是週四，就從今天算起? 還是下週? 這裡設為: 如果今天是週四且未過期，含今天)
      let day = baseDate.getDay();
      let diff = 4 - day; // 4 is Thursday
      if (diff < 0) diff += 7; // 已經過了週四，算下週
      
      baseDate.setDate(baseDate.getDate() + diff);

      for (let i = 0; i < count; i++) {
        let d = new Date(baseDate);
        d.setDate(baseDate.getDate() + (i * 7));
        dates.push(d);
      }
      return dates;
    }

    function formatDate(dateObj) {
      return `${dateObj.getFullYear()}/${String(dateObj.getMonth() + 1).padStart(2, '0')}/${String(dateObj.getDate()).padStart(2, '0')}`;
    }

    // --- API 通訊 ---
    async function apiCall(action, data = {}) {
        document.getElementById('loading-overlay').classList.remove('hidden');
        try {
            // Google Apps Script requires no-cors for simple fetches, or POST with redirect handling
            // 這裡使用 POST 搭配 text/plain 避免 CORS 預檢請求問題
            const response = await fetch(GAS_URL + "?action=" + action, {
                method: "POST",
                body: JSON.stringify(data)
            });
            const result = await response.json();
            return result;
        } catch (e) {
            console.error(e);
            showToast("連線錯誤", "error");
            return null;
        } finally {
            document.getElementById('loading-overlay').classList.add('hidden');
        }
    }

    async function fetchMembers() {
        document.getElementById('loading-overlay').classList.remove('hidden');
        try {
            const response = await fetch(GAS_URL + "?action=read");
            const data = await response.json();
            membersData = data;
            renderMembers();
        } catch (e) {
            console.error(e);
            showToast("讀取資料失敗", "error");
        } finally {
            document.getElementById('loading-overlay').classList.add('hidden');
        }
    }

    // --- UI 渲染 ---
    function renderMembers() {
        const list = document.getElementById('members-list');
        const warningList = document.getElementById('warning-list');
        const warningSection = document.getElementById('warning-section');
        
        // 排序：建立時間新的在上面
        membersData.sort((a, b) => new Date(b.created_at) - new Date(a.created_at));

        // 統計
        let totalRev = 0;
        membersData.forEach(m => totalRev += parseInt(m.amount));
        document.getElementById('total-members').innerText = membersData.length;
        document.getElementById('total-revenue').innerText = "$" + totalRev;

        // 清空列表
        list.innerHTML = "";
        warningList.innerHTML = "";
        
        let hasWarning = false;

        if(membersData.length === 0) {
            list.innerHTML = `<div class="text-center py-12 text-emerald-200/50">尚無資料</div>`;
            return;
        }

        membersData.forEach(m => {
            const remaining = parseInt(m.remaining_sessions);
            const dates = getNextThursdays(remaining, m.start_date);
            
            // 警告名單
            if (remaining <= 2 && remaining > 0) {
                hasWarning = true;
                warningList.innerHTML += `
                <div class="flex items-center justify-between bg-amber-500/10 rounded-lg px-4 py-2">
                    <span class="text-white font-medium">${m.name}</span>
                    <span class="text-amber-300 font-bold">剩餘 ${remaining} 次</span>
                </div>`;
            }

            // 主要卡片
            const statusClass = remaining <= 0 ? 'from-rose-500/20 to-rose-600/20 border-rose-400/30' :
                              remaining <= 2 ? 'from-amber-500/20 to-amber-600/20 border-amber-400/30' :
                              'from-white/5 to-white/10 border-white/10';
            
            const badgeClass = remaining <= 0 ? 'bg-rose-500/30 text-rose-300' :
                             remaining <= 2 ? 'bg-amber-500/30 text-amber-300' :
                             'bg-emerald-500/30 text-emerald-300';

            const card = document.createElement('div');
            card.className = `bg-gradient-to-r ${statusClass} rounded-xl p-4 border fade-in mb-3`;
            card.innerHTML = `
                <div class="flex flex-wrap items-start justify-between gap-4">
                    <div class="flex-1 min-w-0">
                        <div class="flex items-center gap-3 mb-2">
                            <h3 class="text-lg font-bold text-white truncate">${m.name}</h3>
                            <span class="px-3 py-1 rounded-full text-sm font-medium ${badgeClass}">剩餘 ${remaining} 次</span>
                        </div>
                        <div class="text-sm text-emerald-200 mb-2">
                            累計: $${m.amount}
                        </div>
                        ${remaining > 0 ? `
                        <div class="flex flex-wrap gap-2">
                             ${dates.slice(0, 3).map(d => `<span class="px-2 py-1 rounded-lg bg-white/10 text-white text-xs">${formatDate(d)}</span>`).join('')}
                             ${dates.length > 3 ? `<span class="text-xs text-white/50 self-center">...</span>` : ''}
                        </div>` : ''}
                    </div>
                    <div class="flex gap-2">
                        <button onclick="handleTopUp('${m.id}', '${m.name}', ${m.amount}, ${remaining}, '${m.start_date}')" class="px-3 py-2 bg-emerald-500/30 hover:bg-emerald-500/50 text-emerald-300 rounded-lg text-sm">續費</button>
                        <button onclick="handleUse('${m.id}', ${m.amount}, ${remaining}, '${m.start_date}')" class="px-3 py-2 bg-cyan-500/30 hover:bg-cyan-500/50 text-cyan-300 rounded-lg text-sm" ${remaining<=0?'disabled opacity-50':''}>使用</button>
                        <button onclick="openDelete('${m.id}', '${m.name}')" class="px-3 py-2 bg-rose-500/30 hover:bg-rose-500/50 text-rose-300 rounded-lg text-sm">刪</button>
                    </div>
                </div>
            `;
            list.appendChild(card);
        });

        if (hasWarning) {
            warningSection.classList.remove('hidden');
        } else {
            warningSection.classList.add('hidden');
        }
    }

    // --- 操作邏輯 ---
    // 1. 新增 / 續費 (判斷是否為舊人)
    document.getElementById('add-form').addEventListener('submit', async (e) => {
        e.preventDefault();
        const name = document.getElementById('member-name').value.trim();
        const amount = parseInt(document.getElementById('payment-amount').value);
        if(!name) return showToast("請輸入姓名", "error");

        // 檢查是否已存在
        const existing = membersData.find(m => m.name === name);
        
        if (existing) {
            // 舊會員續費
            await handleTopUp(existing.id, existing.name, parseInt(existing.amount), parseInt(existing.remaining_sessions), existing.start_date, amount);
        } else {
            // 新會員
            const sessions = calculateSessions(amount);
            const now = new Date().toISOString();
            const res = await apiCall('create', {
                name: name,
                amount: amount,
                remaining_sessions: sessions,
                start_date: now,
                created_at: now
            });
            if(res && res.status === 'success') {
                showToast(`新增成功: ${name}`);
                document.getElementById('member-name').value = '';
                fetchMembers();
            }
        }
    });

    // 2. 續費功能
    async function handleTopUp(id, name, oldAmount, oldRemaining, oldStartDate, topUpAmount = null) {
        if (!topUpAmount) {
            // 如果是點擊按鈕進來的，使用當前輸入框的值
            topUpAmount = parseInt(document.getElementById('payment-amount').value);
        }
        
        const addedSessions = calculateSessions(topUpAmount);
        const newAmount = oldAmount + topUpAmount;
        const newRemaining = oldRemaining + addedSessions;
        
        // 如果原本已經過期，Start Date 更新為現在，否則保持 (或是依需求更新)
        let newStartDate = oldStartDate;
        if (oldRemaining <= 0) {
            newStartDate = new Date().toISOString();
        }

        const res = await apiCall('update', {
            id: id,
            amount: newAmount,
            remaining_sessions: newRemaining,
            start_date: newStartDate
        });

        if(res && res.status === 'success') {
            showToast(`${name} 續費成功 +${addedSessions}次`);
            fetchMembers();
        }
    }

    // 3. 使用一次
    async function handleUse(id, currentAmount, currentRemaining, startDate) {
        if (currentRemaining <= 0) return;
        const res = await apiCall('update', {
            id: id,
            amount: currentAmount, // 金額不變
            remaining_sessions: currentRemaining - 1,
            start_date: startDate
        });
        if(res && res.status === 'success') {
            showToast(`已扣除 1 次`);
            fetchMembers();
        }
    }

    // 4. 刪除
    function openDelete(id, name) {
        pendingDeleteId = id;
        document.getElementById('delete-name').innerText = name;
        document.getElementById('delete-modal').classList.remove('hidden');
        document.getElementById('delete-modal').classList.add('flex');
    }

    document.getElementById('confirm-delete').addEventListener('click', async () => {
        if(!pendingDeleteId) return;
        const res = await apiCall('delete', { id: pendingDeleteId });
        if(res && res.status === 'success') {
            showToast("已刪除");
            document.getElementById('delete-modal').classList.add('hidden');
            document.getElementById('delete-modal').classList.remove('flex');
            fetchMembers();
        }
    });

    document.getElementById('cancel-delete').addEventListener('click', () => {
        document.getElementById('delete-modal').classList.add('hidden');
        document.getElementById('delete-modal').classList.remove('flex');
    });

    // --- 輔助功能 ---
    function showToast(msg, type='success') {
        const toast = document.createElement('div');
        toast.className = `fixed bottom-4 right-4 px-6 py-3 rounded-xl font-medium z-50 fade-in ${type==='success'?'bg-emerald-500 text-white':'bg-rose-500 text-white'}`;
        toast.innerText = msg;
        document.getElementById('toast-container').appendChild(toast);
        setTimeout(()=>toast.remove(), 3000);
    }

    // 金額按鈕
    const amtInput = document.getElementById('payment-amount');
    document.getElementById('increase-btn').onclick = () => {
        amtInput.value = parseInt(amtInput.value) + 100;
        updatePreview();
    };
    document.getElementById('decrease-btn').onclick = () => {
        if(parseInt(amtInput.value) > 100) amtInput.value = parseInt(amtInput.value) - 100;
        updatePreview();
    };
    function updatePreview() {
        document.getElementById('sessions-preview').innerText = Math.floor(parseInt(amtInput.value)/100) + " 次";
    }
    amtInput.onchange = updatePreview;

    // 初始化
    fetchMembers();

  </script>
 </body>
</html>
