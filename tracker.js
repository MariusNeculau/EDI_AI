/**
 * EDI AI - Progress Tracking System
 * ================================
 * Sistem centralizat pentru urmărirea progresului lui Aidy
 * 
 * Funcționalități:
 * - Salvare automată în localStorage (persistentă pe device)
 * - Metrici per exercițiu: acuratețe, timp răspuns, streak-uri
 * - Export date pentru rapoarte
 * - Istoric sesiuni pentru comparații before/after
 */

const EdiTracker = {
    // Versiunea sistemului de tracking
    VERSION: '1.0.0',
    
    // Cheia pentru localStorage
    STORAGE_KEY: 'edi_ai_progress',
    
    // Sesiunea curentă
    currentSession: null,
    
    /**
     * Inițializează trackerul
     * Apelează la începutul fiecărui exercițiu
     */
    init: function(exerciseType) {
        this.currentSession = {
            id: this.generateSessionId(),
            exerciseType: exerciseType,
            startTime: new Date().toISOString(),
            endTime: null,
            trials: [],
            summary: {
                totalTrials: 0,
                correctTrials: 0,
                incorrectTrials: 0,
                accuracy: 0,
                averageResponseTime: 0,
                maxStreak: 0,
                currentStreak: 0,
                levelReached: 1
            }
        };
        
        console.log(`[EdiTracker] Session started: ${exerciseType}`);
        return this.currentSession.id;
    },
    
    /**
     * Înregistrează o încercare (trial)
     * @param {object} trialData - Datele încercării
     */
    recordTrial: function(trialData) {
        if (!this.currentSession) {
            console.warn('[EdiTracker] No active session. Call init() first.');
            return;
        }
        
        const trial = {
            trialNumber: this.currentSession.trials.length + 1,
            timestamp: new Date().toISOString(),
            target: trialData.target || '',           // Ce trebuia să aleagă
            selected: trialData.selected || '',        // Ce a ales
            isCorrect: trialData.isCorrect || false,
            responseTime: trialData.responseTime || 0, // În milisecunde
            level: trialData.level || 1,
            attempts: trialData.attempts || 1          // Câte încercări până la corect
        };
        
        this.currentSession.trials.push(trial);
        this.updateSummary(trial);
        
        // Auto-save după fiecare trial
        this.saveToStorage();
        
        console.log(`[EdiTracker] Trial recorded: ${trial.isCorrect ? '✓' : '✗'} | Target: ${trial.target}`);
        
        return trial;
    },
    
    /**
     * Actualizează summary-ul sesiunii
     */
    updateSummary: function(trial) {
        const summary = this.currentSession.summary;
        
        summary.totalTrials++;
        
        if (trial.isCorrect) {
            summary.correctTrials++;
            summary.currentStreak++;
            if (summary.currentStreak > summary.maxStreak) {
                summary.maxStreak = summary.currentStreak;
            }
        } else {
            summary.incorrectTrials++;
            summary.currentStreak = 0;
        }
        
        // Calculează acuratețea
        summary.accuracy = Math.round((summary.correctTrials / summary.totalTrials) * 100);
        
        // Calculează timpul mediu de răspuns
        const totalTime = this.currentSession.trials.reduce((sum, t) => sum + (t.responseTime || 0), 0);
        summary.averageResponseTime = Math.round(totalTime / summary.totalTrials);
        
        // Actualizează nivelul maxim atins
        if (trial.level > summary.levelReached) {
            summary.levelReached = trial.level;
        }
    },
    
    /**
     * Încheie sesiunea curentă
     */
    endSession: function() {
        if (!this.currentSession) {
            console.warn('[EdiTracker] No active session to end.');
            return null;
        }
        
        this.currentSession.endTime = new Date().toISOString();
        
        // Calculează durata totală
        const start = new Date(this.currentSession.startTime);
        const end = new Date(this.currentSession.endTime);
        this.currentSession.summary.totalDuration = Math.round((end - start) / 1000); // în secunde
        
        this.saveToStorage();
        
        console.log(`[EdiTracker] Session ended. Accuracy: ${this.currentSession.summary.accuracy}%`);
        
        const completedSession = this.currentSession;
        this.currentSession = null;
        
        return completedSession;
    },
    
    /**
     * Salvează datele în localStorage
     */
    saveToStorage: function() {
        try {
            let allData = this.getAllData();
            
            // Găsește sau adaugă sesiunea curentă
            const existingIndex = allData.sessions.findIndex(s => s.id === this.currentSession.id);
            
            if (existingIndex >= 0) {
                allData.sessions[existingIndex] = this.currentSession;
            } else {
                allData.sessions.push(this.currentSession);
            }
            
            allData.lastUpdated = new Date().toISOString();
            
            localStorage.setItem(this.STORAGE_KEY, JSON.stringify(allData));
            
        } catch (e) {
            console.error('[EdiTracker] Error saving to localStorage:', e);
        }
    },
    
    /**
     * Obține toate datele salvate
     */
    getAllData: function() {
        try {
            const stored = localStorage.getItem(this.STORAGE_KEY);
            if (stored) {
                return JSON.parse(stored);
            }
        } catch (e) {
            console.error('[EdiTracker] Error reading from localStorage:', e);
        }
        
        // Structura implicită
        return {
            version: this.VERSION,
            childName: 'Aidy',
            createdAt: new Date().toISOString(),
            lastUpdated: new Date().toISOString(),
            sessions: []
        };
    },
    
    /**
     * Obține statistici pentru un anumit tip de exercițiu
     */
    getExerciseStats: function(exerciseType) {
        const allData = this.getAllData();
        const sessions = allData.sessions.filter(s => s.exerciseType === exerciseType);
        
        if (sessions.length === 0) {
            return null;
        }
        
        // Calculează statistici agregate
        const totalTrials = sessions.reduce((sum, s) => sum + s.summary.totalTrials, 0);
        const correctTrials = sessions.reduce((sum, s) => sum + s.summary.correctTrials, 0);
        const totalSessions = sessions.length;
        
        // Progres în timp (ultimele 7 sesiuni)
        const recentSessions = sessions.slice(-7);
        const progressTrend = recentSessions.map(s => ({
            date: s.startTime,
            accuracy: s.summary.accuracy,
            level: s.summary.levelReached
        }));
        
        return {
            exerciseType: exerciseType,
            totalSessions: totalSessions,
            totalTrials: totalTrials,
            totalCorrect: correctTrials,
            overallAccuracy: totalTrials > 0 ? Math.round((correctTrials / totalTrials) * 100) : 0,
            bestStreak: Math.max(...sessions.map(s => s.summary.maxStreak)),
            highestLevel: Math.max(...sessions.map(s => s.summary.levelReached)),
            averageAccuracy: Math.round(sessions.reduce((sum, s) => sum + s.summary.accuracy, 0) / totalSessions),
            progressTrend: progressTrend,
            lastSession: sessions[sessions.length - 1]
        };
    },
    
    /**
     * Obține un rezumat complet al progresului
     */
    getProgressSummary: function() {
        const allData = this.getAllData();
        const exerciseTypes = [...new Set(allData.sessions.map(s => s.exerciseType))];
        
        const summary = {
            childName: allData.childName,
            totalSessions: allData.sessions.length,
            firstSession: allData.sessions.length > 0 ? allData.sessions[0].startTime : null,
            lastSession: allData.sessions.length > 0 ? allData.sessions[allData.sessions.length - 1].startTime : null,
            exerciseBreakdown: {},
            overallProgress: {
                totalTrials: 0,
                totalCorrect: 0,
                overallAccuracy: 0
            }
        };
        
        // Statistici per exercițiu
        exerciseTypes.forEach(type => {
            summary.exerciseBreakdown[type] = this.getExerciseStats(type);
        });
        
        // Totale generale
        summary.overallProgress.totalTrials = allData.sessions.reduce((sum, s) => sum + s.summary.totalTrials, 0);
        summary.overallProgress.totalCorrect = allData.sessions.reduce((sum, s) => sum + s.summary.correctTrials, 0);
        
        if (summary.overallProgress.totalTrials > 0) {
            summary.overallProgress.overallAccuracy = Math.round(
                (summary.overallProgress.totalCorrect / summary.overallProgress.totalTrials) * 100
            );
        }
        
        return summary;
    },
    
    /**
     * Exportă datele ca JSON (pentru rapoarte)
     */
    exportData: function() {
        const allData = this.getAllData();
        allData.exportedAt = new Date().toISOString();
        return JSON.stringify(allData, null, 2);
    },
    
    /**
     * Șterge toate datele (cu confirmare)
     */
    clearAllData: function(confirm = false) {
        if (!confirm) {
            console.warn('[EdiTracker] Call clearAllData(true) to confirm deletion.');
            return false;
        }
        
        localStorage.removeItem(this.STORAGE_KEY);
        console.log('[EdiTracker] All data cleared.');
        return true;
    },
    
    /**
     * Generează un ID unic pentru sesiune
     */
    generateSessionId: function() {
        return 'session_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
    },
    
    /**
     * Helper: Obține timpul curent pentru măsurarea răspunsului
     */
    startTimer: function() {
        return Date.now();
    },
    
    /**
     * Helper: Calculează timpul de răspuns
     */
    getResponseTime: function(startTime) {
        return Date.now() - startTime;
    }
};

// Exportă pentru utilizare în browser
if (typeof window !== 'undefined') {
    window.EdiTracker = EdiTracker;
}

// Exportă pentru Node.js (dacă e cazul)
if (typeof module !== 'undefined' && module.exports) {
    module.exports = EdiTracker;
}

console.log('[EdiTracker] Module loaded. Version:', EdiTracker.VERSION);
